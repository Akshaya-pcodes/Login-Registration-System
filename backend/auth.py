import sqlite3
import re
from pathlib import Path

from flask import Blueprint, request, jsonify, session
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

# Create authentication blueprint
auth = Blueprint("auth", __name__)

# Database path
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "users.db"


# ---------------- REGISTER ----------------

@auth.route("/register", methods=["POST"])
def register():

    data = request.get_json(silent=True) or {}

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    # Check required fields
    if not all(
        isinstance(value, str) and value.strip()
        for value in (name, email, password)
    ):
        return jsonify({
            "error": "All fields are required"
        }), 400

    name = name.strip()
    email = email.strip().lower()

    # Validate name
    if len(name) < 3:
        return jsonify({
            "error": "Name must contain at least 3 characters"
        }), 400

    # Validate email
    if not re.fullmatch(
        r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+",
        email
    ):
        return jsonify({
            "error": "Enter a valid email address"
        }), 400

    # Validate password length
    if len(password) < 8:
        return jsonify({
            "error": "Password must be at least 8 characters"
        }), 400

    # Password strength validation
    if (
        not re.search(r"[A-Z]", password)
        or not re.search(r"[a-z]", password)
        or not re.search(r"\d", password)
    ):
        return jsonify({
            "error": "Password must contain uppercase, lowercase and a number"
        }), 400

    # Hash password
    password_hash = generate_password_hash(password)

    try:
        with sqlite3.connect(DB_PATH) as connection:

            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO users (name, email, password_hash)
                VALUES (?, ?, ?)
            """, (name, email, password_hash))

        return jsonify({
            "message": "Registration successful!"
        }), 201

    except sqlite3.IntegrityError:
        return jsonify({
            "error": "Email already exists"
        }), 409


# ---------------- LOGIN ----------------

@auth.route("/login", methods=["POST"])
def login():

    data = request.get_json(silent=True) or {}

    email = data.get("email")
    password = data.get("password")

    # Check required fields
    if (
        not isinstance(email, str)
        or not email.strip()
        or not isinstance(password, str)
        or not password
    ):
        return jsonify({
            "error": "Email and password are required"
        }), 400

    email = email.strip().lower()

    # Find user in database
    with sqlite3.connect(DB_PATH) as connection:

        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, name, email, password_hash
            FROM users
            WHERE email = ?
        """, (email,))

        user = cursor.fetchone()

    # Check user existence
    if user is None:
        return jsonify({
            "error": "Invalid email or password"
        }), 401

    # Verify password
    stored_password_hash = user[3]

    if not check_password_hash(
        stored_password_hash,
        password
    ):
        return jsonify({
            "error": "Invalid email or password"
        }), 401

    # Create session
    session.clear()
    session["user_id"] = user[0]
    session["user_name"] = user[1]

    return jsonify({
        "message": "Login successful!",
        "user": {
            "id": user[0],
            "name": user[1],
            "email": user[2]
        }
    }), 200


# ---------------- DASHBOARD ----------------

@auth.route("/dashboard", methods=["GET"])
def dashboard():

    # Check whether user is logged in
    if "user_id" not in session:
        return jsonify({
            "error": "Please login first"
        }), 401

    return jsonify({
        "message": "Welcome to your dashboard!",
        "user": {
            "id": session["user_id"],
            "name": session["user_name"]
        }
    }), 200


# ---------------- LOGOUT ----------------

@auth.route("/logout", methods=["POST"])
def logout():

    session.clear()

    return jsonify({
        "message": "Logout successful!"
    }), 200