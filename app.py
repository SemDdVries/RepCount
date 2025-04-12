from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
import json
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from datetime import timedelta

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Generate a secure secret key
app.permanent_session_lifetime = timedelta(days=7)  # Session lasts for 7 days

# Path to store user data
USER_DATA_FILE = 'user_data.json'

# Create user data file if it doesn't exist
if not os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, 'w') as f:
        json.dump({}, f)

def load_users():
    """Load user data from file"""
    try:
        with open(USER_DATA_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def save_users(users):
    """Save user data to file"""
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(users, f, indent=4)

@app.route('/')
def home():
    """Home page route"""
    if 'username' in session:
        # User is logged in
        return render_template('dashboard.html', username=session['username'])
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = 'remember' in request.form
        
        users = load_users()
        
        if username in users and check_password_hash(users[username]['password'], password):
            # Successful login
            session.permanent = remember
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            # Failed login
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        email = request.form['email']
        
        # Form validation
        users = load_users()
        error = None
        
        if username in users:
            error = 'Username already exists'
        elif password != confirm_password:
            error = 'Passwords do not match'
        elif len(password) < 8:
            error = 'Password must be at least 8 characters long'
        
        if error:
            flash(error, 'danger')
            return render_template('register.html')
        
        # Create new user with hashed password
        hashed_password = generate_password_hash(password)
        users[username] = {
            'password': hashed_password,
            'email': email,
            'profile': {
                'name': '',
                'weight': '',
                'height': '',
                'goals': []
            }
        }
        
        save_users(users)
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    """Handle user logout"""
    session.pop('username', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    """User dashboard after login"""
    if 'username' not in session:
        flash('Please login first', 'warning')
        return redirect(url_for('login'))
    
    username = session['username']
    users = load_users()
    user_data = users.get(username, {})
    
    return render_template('dashboard.html', username=username, user_data=user_data)

if __name__ == '__main__':
    # Make sure templates folder exists
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    app.run(debug=True) 