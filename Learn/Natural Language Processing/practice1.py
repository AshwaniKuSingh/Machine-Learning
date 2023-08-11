from PyPDF2 import PdfReader

reader = PdfReader("building-the-ai-bank-of-the-future.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()