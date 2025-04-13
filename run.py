import os
import sys
from app import create_app
from app.config.ssl import create_ssl_context

def run_app(use_https=True, port=None):
    """Run the RepCount app with either HTTP or HTTPS"""
    # Create the Flask application
    app = create_app()
    
    if use_https:
        # Create SSL context
        ssl_context = create_ssl_context()
        
        # Default HTTPS port
        if port is None:
            port = 443
        
        print(f"Running with HTTPS on port {port}")
        print("You can access the app at:")
        print(f"  - https://localhost:{port}")
        print(f"  - https://repcount.local:{port if port != 443 else ''}")
        print("\nNOTE: Since we're using a self-signed certificate, you'll need to accept the security warning in your browser.")
        
        app.run(debug=True, host='0.0.0.0', port=port, ssl_context=ssl_context)
    else:
        # Default HTTP port
        if port is None:
            port = 5000
        
        print(f"Running with HTTP on port {port}")
        print("You can access the app at:")
        print(f"  - http://localhost:{port}")
        print(f"  - http://repcount.local:{port if port != 80 else ''}")
        
        app.run(debug=True, host='0.0.0.0', port=port)

if __name__ == '__main__':
    # Parse command line arguments
    use_https = True
    port = None
    
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if arg == '--http':
                use_https = False
            elif arg.startswith('--port='):
                try:
                    port = int(arg.split('=')[1])
                except ValueError:
                    print(f"Invalid port number: {arg}")
                    sys.exit(1)
    
    run_app(use_https, port) 