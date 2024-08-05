from docx import Document

def read_template(template_path):
    # Open the Word file
    doc = Document(template_path)
    return doc