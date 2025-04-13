# RepCount
Make an application that tracks your gym progress, including exercises, weight (goals), set and rep counters and more.

## Features

- **User Authentication System**: Secure login and registration system with password encryption
- **Progress Tracking**: Track workouts, sets, reps, and weights
- **Goal Setting**: Set and monitor fitness goals
- **User Profiles**: Maintain personal fitness information
- **Dark Mode Support**: Toggle between light and dark themes with high contrast ratios that comply with EEA accessibility standards
- **HTTPS Support**: Secure connection with SSL/TLS encryption
- **Custom Hostname**: Easy access via a friendly domain name (repcount.local)

## Project Structure

```
RepCount/
├── app/                        # Main application package
│   ├── __init__.py            # Application factory
│   ├── config/                # Configuration modules
│   │   └── ssl.py             # SSL configuration
│   ├── models/                # Data models
│   │   └── user.py            # User model
│   ├── routes/                # Route definitions
│   │   ├── auth.py            # Authentication routes
│   │   └── main.py            # Main application routes
│   ├── static/                # Static files (CSS, JS, images)
│   │   └── css/
│   │       └── styles.css     # Custom stylesheet
│   └── templates/             # Jinja2 templates
│       ├── base.html          # Base template
│       ├── dashboard.html     # Dashboard template
│       ├── index.html         # Homepage template
│       ├── login.html         # Login template
│       └── register.html      # Registration template
│
├── data/                      # Data storage
│   └── user_data.json         # User data storage
│
├── scripts/                   # Utility scripts
│   ├── admin/                 # Administrative scripts
│   │   ├── setup_admin.py     # Admin privileges helper
│   │   ├── setup_hosts.bat    # Windows hosts setup
│   │   └── setup_hosts.py     # Hosts file configuration
│   └── runners/               # Runner scripts
│       ├── run_http.bat       # HTTP runner (Windows)
│       ├── run_http.sh        # HTTP runner (Unix)
│       ├── run_https.bat      # HTTPS runner (Windows)
│       └── run_https.sh       # HTTPS runner (Unix)
│
├── ssl/                       # SSL certificates
│   ├── cert.pem               # Certificate
│   └── key.pem                # Private key
│
├── run.py                     # Main application runner
├── dev.py                     # Development server
├── setup.bat                  # Windows setup shortcut
├── setup.sh                   # Unix setup shortcut
├── run_http.bat               # Windows HTTP shortcut
├── run_http.sh                # Unix HTTP shortcut
├── run_https.bat              # Windows HTTPS shortcut
├── run_https.sh               # Unix HTTPS shortcut
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Technical Details

The application is built using:
- **Python**: Core programming language
- **Flask**: Web framework for the application
- **Werkzeug Security**: For password hashing and verification
- **JSON**: For storing user data securely
- **CSS Variables**: For theme switching capabilities
- **SSL/TLS**: For secure HTTPS connections

## Setup and Installation

1. Clone the repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. (Optional but recommended) Set up a custom hostname for easier access:
   - **Windows**: Double-click `setup.bat`
   - **Linux/Mac**: Run `chmod +x setup.sh && ./setup.sh`

4. Start the application:
   - **Windows**: 
     - Double-click `run_https.bat` for HTTPS mode (port 443)
     - Double-click `run_http.bat` for HTTP mode (port 5000)
   - **Linux/Mac**: 
     - Run `chmod +x run_https.sh run_http.sh`
     - Run `./run_https.sh` for HTTPS mode (port 443)
     - Run `./run_http.sh` for HTTP mode (port 5000)

5. Access the application:
   - HTTPS mode: `https://repcount.local` (no port needed) or `https://localhost:443`
   - HTTP mode: `http://repcount.local:5000` or `http://localhost:5000`

**Note**: When accessing the app via HTTPS, you'll need to accept the security warning in your browser since we're using a self-signed certificate.

## Security

- Passwords are securely hashed using Werkzeug's security functions
- User data is stored in a JSON file with proper access controls
- Session management for secure user authentication
- HTTPS encryption for secure data transmission

## Accessibility

- High contrast themes with ratios compliant with EEA accessibility standards
- Semantic HTML elements for better screen reader compatibility
- Keyboard navigable interface
- Friendly custom domain name for easier access

## Future Enhancements

- Integration with fitness APIs
- Graphical representation of progress
- Mobile application
- Social sharing features
- OAuth integration with Google/Facebook

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
