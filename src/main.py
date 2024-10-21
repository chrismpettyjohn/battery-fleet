import subprocess

def run_simulation():
    # Run the battery simulation (api.py)
    subprocess.Popen(['python3', 'api.py'])

def run_web_dashboard():
    # Run the Flask app (site.py)
    subprocess.Popen(['python3', 'site.py'])

if __name__ == "__main__":
    # Start the simulation and the web server concurrently
    run_simulation()
    run_web_dashboard()

    # Optionally, wait for both processes to complete (if you need to wait/block)
    input("Press Enter to terminate both processes...")
