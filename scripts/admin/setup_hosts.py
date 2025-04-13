import os
import sys
import platform

def is_admin():
    """Check if the script is running with administrator privileges"""
    try:
        if platform.system() == 'Windows':
            return os.windll.shell32.IsUserAnAdmin() != 0
        else:
            return os.geteuid() == 0
    except:
        return False

def add_hosts_entry(hostname='repcount.local'):
    """Add an entry to the hosts file to map hostname to 127.0.0.1"""
    if platform.system() == 'Windows':
        hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
    else:
        hosts_path = '/etc/hosts'
    
    # Read the current hosts file
    try:
        with open(hosts_path, 'r') as f:
            hosts_content = f.read()
    except:
        print(f"Error: Could not read hosts file at {hosts_path}")
        return False
    
    # Check if the entry already exists
    entry = f"127.0.0.1 {hostname}"
    if entry in hosts_content:
        print(f"The hosts entry for {hostname} already exists.")
        return True
    
    # Add the entry to the hosts file
    try:
        with open(hosts_path, 'a') as f:
            f.write(f"\n{entry}")
        print(f"Successfully added {hostname} to your hosts file.")
        print(f"You can now access the app at https://{hostname}")
        return True
    except:
        print(f"Error: Could not write to hosts file at {hosts_path}")
        return False

if __name__ == '__main__':
    if not is_admin():
        print("Error: This script needs to be run with administrator privileges.")
        print("\nOn Windows: Right-click on the script and select 'Run as administrator'")
        print("On Linux/Mac: Run the script with 'sudo python setup_hosts.py'")
        sys.exit(1)
    
    # Get hostname from command line arguments or use default
    hostname = sys.argv[1] if len(sys.argv) > 1 else 'repcount.local'
    
    add_hosts_entry(hostname) 