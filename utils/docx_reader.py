from docx import Document

def extract_text_from_docx(file):
    doc = Document(file)
    text = "\n".join([p.text for p in doc.paragraphs])
    return text
