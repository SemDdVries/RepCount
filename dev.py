from app import create_app

if __name__ == '__main__':
    # Create the application
    app = create_app()
    
    # Run the app in development mode on port 5000
    app.run(debug=True, host='0.0.0.0', port=5000) 