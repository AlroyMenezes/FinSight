#import streamlit as st
def insert_responses(doc, responses):
    placeholders = [
        "Name of the company:",
        "Date of the call:",
        "Key Participants:",
        "Quarterly Results:",
        "Revenue and Growth:",
        "Market and Distribution:",
        "Challenges:",
        "Outlook:"
    ]
    
    # Create a dictionary from placeholders to responses
    response_dict = dict(zip(placeholders, responses))
    #st.write(response_dict)
    

    # Replace placeholders in tables
    for table in doc.tables:
        for row in table.rows:
            flag = 1
            for cell in row.cells:
                original_text = cell.text  # Store the original cell text
                for placeholder, response in response_dict.items():
                    if flag == 1:
                        if placeholder in original_text:  # Check against the original cell text
                            #st.write(f"Replacing placeholder '{placeholder}' with '{response}' in cell: {original_text}")
                            cell.text = cell.text.replace(placeholder, f'{placeholder}\n \n{response}')
                            original_text = cell.text  # Update the original text after replacement
                            flag=0
    
    return doc
