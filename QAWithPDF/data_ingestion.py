# --------------------- Path Setup ---------------------

import sys
import os

# Add the parent directory to the system path to allow relative imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# --------------------- Imports ------------------------

from llama_index.core import SimpleDirectoryReader  # For loading documents
from exception import customexception               # Custom exception handling class
from logger import logging                           # Custom logger for logging messages

# --------------------- Function: load_data ------------------------

def load_data(data):
    """
    Load documents from a specified directory using SimpleDirectoryReader.

    Parameters:
    - data (str): The path to the directory containing documents (PDF, TXT, etc.).

    Returns:
    - documents (list): A list of loaded Document objects.
    """
    try:
        logging.info("Data loading started...")

        # Initialize the document loader for the 'Data' directory
        loader = SimpleDirectoryReader("Data")

        # Load and return documents
        documents = loader.load_data()

        logging.info("Data loading completed.")
        return documents

    except Exception as e:
        logging.info("Exception occurred while loading data.")
        raise customexception(e, sys)
