import streamlit as st
import PyPDF2
from io import BytesIO


def main():
    st.title('Codebase Explainer')

    # Text Area for Code Input
    user_code_input = st.text_area("Paste your code here:")

    # File Uploader for PDF Documentation
    uploaded_file = st.file_uploader("Upload documentation", type=["pdf"])

    # Initial Placeholder for PDF Text
    pdf_text = ""

    if uploaded_file:
        # Read the PDF File
        with BytesIO(uploaded_file.getvalue()) as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in range(len(pdf_reader.pages)):
                pdf_text += pdf_reader.pages[page].extract_text()

    # Display the Extracted Text from PDF
    if pdf_text:
        st.subheader("Extracted Text from DocumentationF:")
        st.write(pdf_text)

    # Handle the Explain Button Click
    if st.button('Explain'):
        if user_code_input or pdf_text:
            st.subheader('Your code explained...')
        else:
            st.warning('Please input some code or upload code documentation first.')


if __name__ == '__main__':
    main()
