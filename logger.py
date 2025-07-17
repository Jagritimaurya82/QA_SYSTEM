'''What this does:
1. Creates a uniquely named .log file with a timestamp.
2. Stores logs in a logs folder.
3. Captures line number, module name, level (INFO, ERROR, etc.), and the actual message in each log entry.
'''
# ------------------------- Logging Setup -------------------------

import logging
import os
from datetime import datetime

# Create a log file name with the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path where logs will be stored (in a folder named 'logs' in the current working directory)
log_path = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it doesn't exist
os.makedirs(log_path, exist_ok=True)

# Full path for the log file
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure the logging module
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO (can be DEBUG, WARNING, ERROR, etc.)
    filename=LOG_FILEPATH,  # Set the log file path
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"  # Log format
)
