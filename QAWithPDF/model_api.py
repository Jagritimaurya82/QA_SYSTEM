# --------------------- Path Setup ---------------------

import sys
import os

# Add parent directory to the system path for relative imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# --------------------- Environment & Module Imports ---------------------

from dotenv import load_dotenv                      # To load environment variables from .env file
from llama_index.llms.gemini import Gemini          # Gemini LLM from LlamaIndex
from IPython.display import Markdown, display       # For displaying outputs in notebooks (optional)
import google.generativeai as genai                 # Google Generative AI SDK
from exception import customexception               # Custom exception class for structured error handling
from logger import logging                          # Logger for logging info and errors

# --------------------- Load Environment Variables ---------------------

load_dotenv()                                       # Load variables from .env file
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")       # Get the Gemini API key from environment variables

# --------------------- Configure Gemini SDK ---------------------

genai.configure(api_key=GOOGLE_API_KEY)            # Set the API key for generative AI usage

# --------------------- Function: load_model ---------------------

def load_model():
    """
    Initializes and returns the Gemini language model.

    Returns:
    - Gemini: An instance of the Gemini class configured with the latest model.
    """
    try:
        logging.info("Loading Gemini LLM model...")
        
        # Initialize Gemini with the latest 1.5 flash model
        model = Gemini(models='models/gemini-1.5-flash-latest', api_key=GOOGLE_API_KEY)
        
        logging.info("Gemini model loaded successfully.")
        return model

    except Exception as e:
        logging.error("Exception occurred while loading Gemini model.")
        raise customexception(e, sys)
