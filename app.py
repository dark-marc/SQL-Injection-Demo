from flask import Flask, request, render_template, redirect, url_for, session, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = '123'

# Initialize the database with sample data.

def init_db():
    conn = sqlite3.connect('vulnerable.db')
    c = conn.cursor()
    # Drop and recreate table to prevent duplicates
    c.execute('DROP TABLE IF EXISTS users')
    c.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, full_name TEXT, email TEXT)')
    # Insert sample users
    users = [
        ('admin', 'password123', 'Admin User', 'admin@example.com'),
        ('user1', 'pass1', 'User One', 'user1@example.com'),
        ('user2', 'pass2', 'User Two', 'user2@example.com'),
        ('user3', 'pass3', 'User Three', 'user3@example.com'),
    ]
    c.executemany("INSERT INTO users (username, password, full_name, email) VALUES (?, ?, ?, ?)", users)
    conn.commit()
    conn.close()

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Dashboard - Page After Login Success
@app.route('/dashboard')
def login_response_page():
    return render_template('login_response.html', user=session)

# Login Route - Handles Authentication
@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    query = f"SELECT id, username, password, full_name, email FROM users WHERE username = '{username}' AND password = '{password}'"    
    conn = sqlite3.connect('vulnerable.db')
    c = conn.cursor()
    try:
        c.execute(query)
        user = c.fetchone()
        conn.close()
        
        if user:
            session['username'] = user[1]
            session['full_name'] = user[3]
            session['email'] = user[4]
            session['command'] = query
            return jsonify(success=True, redirect=url_for('login_response_page'))

        else:
            return jsonify(success=False, error="Invalid credentials. Please try again.")
            
    except sqlite3.Error:
        conn.close()
        return jsonify(success=False, error="An error occurred. Please try again.")

# Logout Route
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('full_name', None)
    session.pop('email', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5011)
