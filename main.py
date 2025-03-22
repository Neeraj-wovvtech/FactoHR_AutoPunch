from datetime import datetime
from src import encrypt
import os, sys, logging, pytz, subprocess

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define execution time ranges
LOGIN_TIME_RANGE = ("09:20", "10:00")
LOGOUT_TIME_RANGE = ("19:30", "20:00")

def check_and_store_credentials():
    """If .env file doesn't exist, ask for username, password, and FactoHR URL, then encrypt them."""
    if not os.path.exists(".env"):
        logging.info("No .env file found. Requesting credentials...")
        
        url = input("Enter your FactoHR company URL: ").strip()
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        logging.info("Encrypting credentials and storing in .env...")
        encrypt.encrypt_credentials(username, password)

        # Append the FactoHR URL to .env
        with open(".env", "a") as env_file:
            env_file.write(f"URL={url}\n")

        logging.info("Credentials and URL stored securely.")
    else:
        logging.info(".env file already exists. Skipping credential setup.")

def is_time_in_range(start, end):
    """Check if the current time is within the specified range."""
    current_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%H:%M")
    logging.debug(f"Current time is {current_time}. Checking against range: {start} - {end}.")
    return start <= current_time <= end

def run_script(script_path):
    """Run the specified script using the Python from the activated virtual environment."""
    venv_python = sys.executable  # Gets the currently activated venv Python

    logging.info(f"Executing {script_path} using {venv_python}...")
    try:
        result = subprocess.run([venv_python, script_path], check=True, capture_output=True, text=True)
        logging.info(f"Output of {script_path}:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while executing {script_path}: {e.stderr}")


if __name__ == "__main__":
    # Step 1: Ensure credentials and URL are securely stored
    check_and_store_credentials()

    # Step 2: Determine if we should run login or logout script
    current_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%H:%M")
    logging.info(f"Current time is {current_time}.")
    if is_time_in_range(*LOGIN_TIME_RANGE):
        logging.info(f"Current time {current_time} is within the login time range.")
        run_script("src/autoLogin.py")
    elif is_time_in_range(*LOGOUT_TIME_RANGE):
        logging.info(f"Current time {current_time} is within the logout time range.")
        run_script("src/autoLogout.py")
    else:
        logging.warning(f"Current time {current_time} is not within the scheduled time range. Exiting...")