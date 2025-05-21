# SQL Injection Demo

## Overview
This Flask web application demonstrates SQL injection vulnerabilities in a user authentication system. It includes an SQLite database and illustrates how improperly constructed SQL queries can be exploited.

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
