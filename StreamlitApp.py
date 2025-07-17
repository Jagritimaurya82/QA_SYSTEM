# Import necessary libraries
import streamlit as st
from QAWithPDF.data_ingestion import load_data        # Function to load documents
from QAWithPDF.embedding import download_gemini_embedding  # Function to embed documents
from QAWithPDF.model_api import load_model            # Function to load the LLM model

# Main function to run the Streamlit app
def main():
    # Set the page configuration (e.g., title)
    st.set_page_config("QA with Documents")
    
    # File uploader to allow users to upload their own PDF/document
    doc = st.file_uploader("Upload your document")

    # Header for the app
    st.header("QA with Documents (Information Retrieval)")
    
    # Input field to let the user ask a question
    user_question = st.text_input("Ask your question")

    # Button to trigger processing and querying
    if st.button("Submit & Process"):
        with st.spinner("Processing..."):
            # Load the uploaded document(s)
            document = load_data(doc)
            
            # Load the Gemini LLM model
            model = load_model()
            
            # Create query engine by embedding the document using Gemini embeddings
            query_engine = download_gemini_embedding(model, document)
                
            # Query the document with the user's question
            response = query_engine.query(user_question)
                
            # Display the model's response to the question
            st.write(response.response)

# Entry point for the Streamlit app
if __name__ == "__main__":
    main()
