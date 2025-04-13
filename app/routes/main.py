from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.user import load_users

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    """Home page route"""
    if 'username' in session:
        # User is logged in
        return redirect(url_for('main.dashboard'))
    return render_template('index.html')

@main_bp.route('/dashboard')
def dashboard():
    """User dashboard after login"""
    if 'username' not in session:
        flash('Please login first', 'warning')
        return redirect(url_for('auth.login'))
    
    username = session['username']
    users = load_users()
    user_data = users.get(username, {})
    
    return render_template('dashboard.html', username=username, user_data=user_data)

@main_bp.route('/toggle-theme')
def toggle_theme():
    """Toggle between light and dark theme"""
    current_theme = session.get('theme')
    if current_theme == 'dark':
        session['theme'] = 'light'
    else:
        session['theme'] = 'dark'
    
    # Redirect back to the current page
    current_page = request.args.get('current_page', '/')
    return redirect(current_page) 