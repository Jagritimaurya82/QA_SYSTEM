# --------------------- Path Setup ---------------------

import sys
import os

# Add the parent directory to the system path to allow relative imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# --------------------- LlamaIndex Imports ---------------------

from llama_index.core import VectorStoreIndex           # For creating vector-based index
from llama_index.core import ServiceContext             # (optional) For passing custom LLM and embedding settings
from llama_index.core import StorageContext, load_index_from_storage  # For saving and loading index
from llama_index.embeddings.gemini import GeminiEmbedding  # Gemini embedding model for vectorization

# --------------------- Project Module Imports ---------------------

from QAWithPDF.data_ingestion import load_data          # Custom function to load documents
from QAWithPDF.model_api import load_model              # Custom function to load LLM

# --------------------- Utility Imports ---------------------

from exception import customexception                   # Custom exception class
from logger import logging                               # Logger for debugging and info tracking

# --------------------- Function: download_gemini_embedding ---------------------

def download_gemini_embedding(model, document):
    """
    Loads the Gemini embedding model, indexes the documents, and creates a query engine.

    Parameters:
    - model: The LLM (e.g., Gemini LLM) used for question-answering
    - document: A list of documents to be indexed

    Returns:
    - query_engine: An instance that allows semantic search over the indexed documents
    """
    try:
        logging.info("Initializing Gemini embedding model...")
        gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")

        # Set global defaults via LlamaIndex Settings
        from llama_index.core import Settings
        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.chunk_size = 800
        Settings.chunk_overlap = 20

        # Create vector index from documents using global settings
        logging.info("Creating vector index from documents...")
        index = VectorStoreIndex.from_documents(document, service_context=Settings)

        # Persist index to local disk for reuse
        logging.info("Persisting index to storage...")
        index.storage_context.persist()

        # Create a query engine for semantic search
        logging.info("Creating query engine for semantic search...")
        query_engine = index.as_query_engine()

        return query_engine

    except Exception as e:
        logging.error("Exception occurred in download_gemini_embedding.")
        raise customexception(e, sys)
