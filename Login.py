from flask import Flask, request, render_template, redirect, url_for
from bcrypt import hashpw, gensalt
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database connection
def db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootme1",
        database="inocen"
    )

@app.route("/")
def index():
    return render("signup.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("Username")
        email = request.form.get("Email")
        password = request.form.get("Password")

        # Validate inputs
        if not username or not email or not password:
            return "<h3>Error: All fields are required!</h3>"

        # Hash the password
        hashed_password = hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

        # Save to database
        try:
            connection = db()
            cursor = connection.cursor()

            query = "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, email, hashed_password))
            connection.commit()

        except mysql.connector.IntegrityError as e:
            if "username" in str(e):
                error_message = "Username already exists. Please choose another."
            elif "email" in str(e):
                error_message = "Email already exists. Please use another."
            else:
                error_message = "An unknown error occurred."
            return f"<h3>Error: {error_message}</h3>"

        except Error as e:
            return f"<h3>Error: Could not save user. {str(e)}</h3>"

        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

    return render("signup.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5500,debug=True)
