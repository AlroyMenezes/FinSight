from template_read import read_template
from response_insert import insert_responses
#import streamlit as st
def generate_report(template_path,ot):
    doc = read_template(template_path)
    #st.write("hi")
    responses = ot 
    updated_doc = insert_responses(doc, responses)
    
    # Save the updated Word file to a new path
    new_path = template_path.replace('.docx', '_updated.docx')
    updated_doc.save(new_path)
    #print(f'Report updated and saved to {new_path}')
    return new_path