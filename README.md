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
   pip install flask
   ```
3. (Optional but recommended) Set up a custom hostname for easier access:
   - Windows: Run `setup_hosts.py` as administrator
   - Linux/Mac: Run `sudo python setup_hosts.py`

4. Start the application:
   - **Windows**: 
     - Double-click `run_app.bat` for HTTPS mode (port 443)
     - Double-click `run_app_http.bat` for HTTP mode (port 5000)
   - **Linux/Mac**: 
     - Run `chmod +x run_app.sh run_app_http.sh` to make scripts executable
     - Run `./run_app.sh` for HTTPS mode (port 443)
     - Run `./run_app_http.sh` for HTTP mode (port 5000)

5. Access the application:
   - HTTPS mode: `https://repcount.local` (no port needed) or `https://localhost:443`
   - HTTP mode: `http://repcount.local:5000` or `http://localhost:5000`

**Note**: When accessing the app via HTTPS, you'll need to accept the security warning in your browser since we're using a self-signed certificate.

## Advanced Usage

You can run the application with custom settings using the `run.py` script:

```
# Run with HTTPS on the default port (443)
python run.py

# Run with HTTP on the default port (5000)
python run.py --http

# Run with HTTPS on a custom port
python run.py --port=8443

# Run with HTTP on a custom port
python run.py --http --port=8080
```

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
