# SQL Injection Demo

## Overview
This Flask web application demonstrates SQL injection vulnerabilities in a user authentication system. It includes an SQLite database and illustrates how improperly constructed SQL queries can be exploited.


![Script](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemZ6b3UydzdnNTVwbWM4eTBmdWptN3d0aDJzaGpnc2pjMmY3eXdhNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pP4k3B4czAGGXHhddA/giphy.gif)


## Features
- User login with predefined credentials.
- Detailed HTML/CSS frontend using Bootstrap.
- Illustrative carousel explaining SQL injection concepts.
- Example inputs to test SQL injection vulnerabilities.
- AJAX-based login form submission for improved user experience.

### Prerequisites
- Python
- Flask
- SQLite

## App Routes

### `/`
- **Method**: GET
- **Description**: Renders the homepage where users can access the login form.

### `/login`
- **Method**: POST
- **Description**: Handles user authentication. It receives a JSON payload containing the username and password, checks credentials against the database, and manages user sessions.

### `/dashboard`
- **Method**: GET
- **Description**: Renders the dashboard page after a successful login, displaying user information.

### `/logout`
- **Method**: GET
- **Description**: Logs the user out by clearing the session data and redirects to the homepage.

## Setup Instructions

1. **Clone or Download the Repository**  
   Clone this repository or download the source code to your local machine.

2. **Create a Virtual Environment**  
   Navigate to the project folder in your terminal or command prompt, then run:
   ```
   python -m venv venv
   ```

4. **Activate the virtual environment:** 
- On Windows:  
  ```
  venv\Scripts\activate
  ```
- On macOS/Linux:  
  ```
  source venv/bin/activate
  ```

4. **Install Dependencies**  

**Install dependencies by running:**
  ```
  pip install Flask
  ```

## How It Works

1. **Starting Up**: 
   - The app sets up a small database with user accounts.

2. **Homepage**: 
   - Users see a login page to enter their details.

3. **Logging In**: 
   - When a user fills out the login form and clicks "Login," the app checks the entered username and password against stored accounts.
   - It sends the inputted information to the app.

4. **Finding Users**: 
   - The app attempts to find a matching user. If successful, the user is logged in and taken to a welcome page. If not, an error message indicates incorrect credentials.

5. **Logging Out**: 
   - Users can log out, returning them to the login page.

6. **SQL Injection Example**: 
   - The app demonstrates how unsafe coding practices can lead to security vulnerabilities. Users can enter specific phrases to bypass the login and gain unauthorized access.

7. **Response Page**: 
   - After a successful login, users are shown a page with their details and the SQL command used for login.

## Running the Script

Execute the script with:
  ```
  python app.py
  ```

The app url will be: http://127.0.0.1:5011/

## Ethical Use

This application is designed solely for educational purposes to demonstrate SQL injection vulnerabilities and enhance understanding of cybersecurity practices. By using this tool, you acknowledge that it is intended for responsible learning. Always adhere to ethical guidelines when exploring security testing and make sure you have permission to test any systems you interact with.
