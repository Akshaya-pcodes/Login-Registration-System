Login & Registration System

A web-based authentication application developed using Python Flask and SQLite. This project provides user registration and login functionality with secure password hashing and session-based authentication.

Overview

The Login & Registration System is designed to provide a simple and user-friendly authentication process. New users can create an account, and registered users can log in to access protected pages.

The application uses Flask for backend development and SQLite for database management.

Features

- User Registration
- User Login
- Password Hashing
- Session-Based Authentication
- SQLite Database Integration
- User Dashboard
- Form Data Validation
- Unique Email Validation

Technologies Used

Technology| Purpose
Python| Backend Programming
Flask| Web Framework
SQLite| Database
HTML5| Page Structure
CSS3| Styling
JavaScript| Frontend Interactions

Project Structure

Login-Registration-System/
│
├── app.py
├── config.py
├── database/
│   └── users.db
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── requirements.txt
├── .gitignore
└── README.md

Note: Adjust the folder structure above to match the actual project files.

Installation and Setup

1. Clone the Repository

git clone https://github.com/Akshaya-pcodes/Login-Registration-System.git

2. Navigate to the Project Folder

cd Login-Registration-System

3. Create a Virtual Environment

python -m venv venv

4. Activate the Virtual Environment

Windows PowerShell:

.\venv\Scripts\Activate.ps1

5. Install Dependencies

pip install -r requirements.txt

6. Run the Application

python app.py

7. Open in Browser

http://127.0.0.1:5000

Database

SQLite is used to store registered user information.

The application uses password hashing instead of storing plain-text passwords.

Application Workflow

1. A new user opens the registration page.
2. The user enters the required details.
3. The application validates the submitted information.
4. The password is hashed before database storage.
5. Registered users can log in using their credentials.
6. Successful authentication creates a user session.
7. The authenticated user can access the dashboard.

Future Improvements

- Password Reset Functionality
- Email Verification
- Improved Input Validation
- User Profile Management
- Enhanced Authentication Security

Author

Akshaya P

GitHub: https://github.com/Akshaya-pcodes

---

Developed as a hands-on web development project to understand backend development, database integration, and authentication workflows.
