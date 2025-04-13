import os
import ssl

def create_ssl_context():
    """Create SSL context with self-signed certificate if certificates don't exist"""
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
    return context 