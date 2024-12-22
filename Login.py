from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# Configure the SQLite database
db = {
    'host': 'localhost',
    'user': 'inocen',
    'password': 'rootme1',
    'database': 'inocen'
}

@app.route('/')

def signup():
    return render_template('signup.html')

# Route to handle form submission and save to database
@app.route('/save_Sign up.html', methods=['POST'])

def save_signup():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']


    # Hash the password for security
    hashed_password = generate_password_hash(password, method='sha256')

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(120), unique=True, nullable=False)
        username = db.Column(db.String(80), unique=True, nullable=False)
        password = db.Column(db.String(200), nullable=False)

    # Save to the database
    new_user = User(email=email, username=username, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return "User registered successfully!"
    except:
        db.session.rollback()
        return "Username already exists or an error occurred."

if __name__ == '__main__':
    app.run(debug=True)
