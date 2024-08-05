import streamlit as st
import os  # For environment variables
from background import add_bg_from_local  # Importing the background function
from pdf_reader import extract_text_from_pdf  # Importing function that extracts text from PDF
from chunks import get_chunks #Importing function that chunks the text
from vector_embeddings import get_vector_store
from gemini import user_input
from report_generation import generate_report

# Adding background image 
add_bg_from_local()

# Streamlit UI
st.title("FinSight")


# Sidebar UI for file upload, centered
st.markdown("<h2 style='text-align: center;'>Upload your Financial Call Transcript here.</h2>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["pdf"], help="Drag and drop a PDF file here or click to upload")

if uploaded_file is not None:
    # Ensure "temp" directory exists
    temp_dir = "temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    file_path = os.path.join(temp_dir, uploaded_file.name)
    
    # Save the uploaded PDF file to the temp directory
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.sidebar.write(f"Uploaded file: {uploaded_file.name}")
    
    # Extract text from the uploaded PDF file
    text = extract_text_from_pdf(file_path)
    
    # Display the extracted text in the sidebar
    st.sidebar.write("Extracted Text:")
    st.sidebar.write(text)

# Generate summary body button

if st.button("Generate Summary"):
    with st.spinner("Generating summary..."):
        text_chunks = get_chunks(text)
        get_vector_store(text_chunks)
        ot = user_input()
    st.success("Summary Generated Successfully!")

    with st.spinner("Generating report..."):
        template_path = "C:/Users/alroy/OneDrive/Documents/AIMIT/SEM 4/Domain Knowledge Project/Client Questionnaire Doc (1).docx"
        updated_doc_path = generate_report(template_path,ot)
    
    # Read the generated report for download
    with open(updated_doc_path, "rb") as file:
        btn = st.download_button(
        label="Download Report",
            data=file,
            file_name="Generated_Report.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
