# RepCount
Make an application that tracks your gym progress, including exercises, weight (goals), set and rep counters and more.

## Features

- **User Authentication System**: Secure login and registration system with password encryption
- **Progress Tracking**: Track workouts, sets, reps, and weights
- **Goal Setting**: Set and monitor fitness goals
- **User Profiles**: Maintain personal fitness information

## Technical Details

The application is built using:
- **Python**: Core programming language
- **Flask**: Web framework for the application
- **Werkzeug Security**: For password hashing and verification
- **JSON**: For storing user data securely

## Setup and Installation

1. Clone the repository
2. Install the required packages:
   ```
   pip install flask
   ```
3. Run the application:
   ```
   python app.py
   ```
4. Access the application at `http://localhost:5000`

## Security

- Passwords are securely hashed using Werkzeug's security functions
- User data is stored in a JSON file with proper access controls
- Session management for secure user authentication

## Future Enhancements

- Integration with fitness APIs
- Graphical representation of progress
- Mobile application
- Social sharing features
- OAuth integration with Google/Facebook

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
