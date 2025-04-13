import json
import os

# Path to store user data
USER_DATA_FILE = 'data/user_data.json'

def load_users():
    """Load user data from file"""
    # Ensure the data directory exists
    os.makedirs(os.path.dirname(USER_DATA_FILE), exist_ok=True)
    
    try:
        with open(USER_DATA_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        # Create a new file if it doesn't exist
        with open(USER_DATA_FILE, 'w') as f:
            json.dump({}, f)
        return {}

def save_users(users):
    """Save user data to file"""
    # Ensure the data directory exists
    os.makedirs(os.path.dirname(USER_DATA_FILE), exist_ok=True)
    
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(users, f, indent=4)