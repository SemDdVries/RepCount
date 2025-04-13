from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import load_users, save_users

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
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
            return redirect(url_for('main.dashboard'))
        else:
            # Failed login
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
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
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    """Handle user logout"""
    session.pop('username', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('main.home')) 