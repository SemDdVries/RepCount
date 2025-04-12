import os
import sys
import ssl
from app import app

def run_app(use_https=True, port=None):
    """Run the RepCount app with either HTTP or HTTPS"""
    if use_https:
        # SSL configuration
        cert_dir = 'ssl'
        cert_file = os.path.join(cert_dir, 'cert.pem')
        key_file = os.path.join(cert_dir, 'key.pem')
        
        # Create certificate directory if it doesn't exist
        if not os.path.exists(cert_dir):
            os.makedirs(cert_dir)
        
        # Generate self-signed certificate if it doesn't exist
        if not (os.path.exists(cert_file) and os.path.exists(key_file)):
            print("Generating self-signed SSL certificate...")
            os.system(f'openssl req -x509 -newkey rsa:4096 -nodes -out {cert_file} -keyout {key_file} '
                      f'-days 365 -subj "/CN=repcount.local"')
        
        # Create SSL context
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(cert_file, key_file)
        
        # Default HTTPS port
        if port is None:
            port = 443
        
        print(f"Running with HTTPS on port {port}")
        print("You can access the app at:")
        print(f"  - https://localhost:{port}")
        print(f"  - https://repcount.local:{port if port != 443 else ''}")
        print("\nNOTE: Since we're using a self-signed certificate, you'll need to accept the security warning in your browser.")
        
        app.run(debug=True, host='0.0.0.0', port=port, ssl_context=context)
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