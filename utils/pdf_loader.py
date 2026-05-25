from PyPDF2 import PdfReader


def load_pdf(file_path):  # Creates reusable function.

    text = ""  # We’ll gradually store all PDF text here.

    reader = PdfReader(file_path)  # Loads PDF into memory.

    for page in reader.pages:        # PDF may contain many pages. We read page-by-page.
        text += page.extract_text()     # Adds each page’s text into one combined string.
 
    return text     # Now entire PDF becomes machine-readable text.