import os
import sys
import ctypes
import subprocess

def is_admin():
    """Check if the current script is running with admin privileges"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin(script_path, *args):
    """Re-run the script with admin privileges"""
    script = os.path.abspath(script_path)
    params = ' '.join([script] + list(args))
    
    # The 'runas' verb requests elevation
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)

if __name__ == '__main__':
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Check if running as admin
    if not is_admin():
        print("Requesting administrator privileges...")
        # Re-run this script with admin rights
        run_as_admin(os.path.join(script_dir, 'setup_hosts.py'))
    else:
        # If we're already admin, run the setup_hosts.py script
        try:
            from setup_hosts import add_hosts_entry
            hostname = sys.argv[1] if len(sys.argv) > 1 else 'repcount.local'
            add_hosts_entry(hostname)
            
            # Keep the window open until user presses Enter
            input("\nPress Enter to close this window...")
        except Exception as e:
            print(f"Error: {e}")
            input("\nAn error occurred. Press Enter to close this window...") 