import streamlit as st
from PIL import Image
import pytesseract

# Title of the app
st.title("Metro Card Scanner")

# Instructions
st.write("""
    Upload an image of your metro card. The app will extract and display the information from the card.
    Please ensure the image is clear and all text is readable.
""")

# File uploader for the metro card image
uploaded_file = st.file_uploader("Choose a metro card image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Metro Card', use_column_width=True)
    
    # OCR: Extract text from the image using pytesseract
    st.write("Extracting information...")
    extracted_text = pytesseract.image_to_string(image)
    
    # Display the extracted text
    st.write("Extracted Information:")
    st.text(extracted_text)

# Security Note
st.write("""
    **Security Notice:** This app does not store any data and is for demonstration purposes only.
    For a production environment, ensure proper security measures are in place, such as:
    - Encrypting uploaded files
    - Using HTTPS
    - Implementing user authentication and authorization
    - Sanitizing and validating all user inputs
""")

# Footer
st.write("© 2024 Metro Card Scanner")

