## FinSightApp

**FinSightApp** is a comprehensive financial analysis application designed to provide insights from financial call transcripts. Using advanced AI models, the application processes uploaded PDFs of financial call transcripts, extracts relevant information, and generates a detailed report.

### Key Features
- **PDF Extraction**: Upload PDFs of financial call transcripts and extract the text efficiently.
- **Text Chunking**: Split the extracted text into manageable chunks for processing.
- **AI-Powered Analysis**: Utilize Google Generative AI for creating embeddings and querying the extracted text.
- **Customizable Questions**: Predefined set of questions to extract critical information from the transcripts.
- **FAISS Vector Store**: Store text chunks and their embeddings in a FAISS vector store for efficient similarity searches.
- **Summary Generation**: Generate concise summaries of key points from the financial call transcripts.
- **Report Generation**: Create detailed reports using a Word template, populated with the extracted information.

### Technology Stack
- **Streamlit**: For creating a user-friendly web interface.
- **PyPDF2**: For extracting text from PDF files.
- **LangChain**: For handling text splitting and embedding creation.
- **Google Generative AI**: For generating embeddings and answering questions.
- **FAISS**: For efficient similarity searches in the text embeddings.
- **Python-docx**: For reading and writing Word documents.

### How to Use
1. **Upload a PDF**: Use the interface to upload a financial call transcript in PDF format.
2. **Extract and Process**: The application extracts text, chunks it, and processes it using AI models.
3. **Generate Summary**: Answer predefined questions to summarize the key points.
4. **Create Report**: Generate a detailed report using a Word template, which can be downloaded.

### Files in the Repository
- **background.py**: Handles the background image setup for the Streamlit interface.
- **chunks.py**: Contains the logic for chunking the extracted text.
- **gemini.py**: Manages the AI-based question answering using Google Generative AI and FAISS.
- **pdf_reader.py**: Extracts text from PDF files.
- **prompt.py**: Defines the prompt template for generating summaries.
- **report_generation.py**: Generates the final report by inserting answers into a Word template.
- **response_insert.py**: Inserts the summarized responses into the Word template.
- **template_read.py**: Reads the Word template for report generation.
- **vector_embeddings.py**: Creates and manages the FAISS vector store for text embeddings.
- **FinSightapp.py**: The main Streamlit application script.

### Future Enhancements
- **Support for Multiple File Formats**: Extend support to other document formats.
- **Custom Questions**: Allow users to define their own questions for analysis.
- **Improved UI/UX**: Enhance the user interface for better user experience.
- **Real-Time Analysis**: Implement real-time processing and analysis capabilities.
