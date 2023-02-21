from docx import Document

document = Document("test.docx")
for paragraph in document.paragraphs:
    if 'C01265980' in paragraph.text:
        paragraph.text = 'Номер РР в СМКСС: 99999.'
        print(paragraph.text)

document.save('update.docx')