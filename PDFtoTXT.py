import PyPDF2

def convert_pdf_to_text(pdf_file_path):
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text

pdf_file_path = input('Enter the name of the PDF file: ')

if pdf_file_path.endswith('.pdf'):
    txt_file_path = pdf_file_path[:-4] + '.txt'
else:
    txt_file_path = pdf_file_path + '.txt'

text = convert_pdf_to_text(pdf_file_path)

with open(txt_file_path, 'w', encoding="utf-8") as txt_file:
    txt_file.write(text)

print(f'Text extracted from {pdf_file_path} and saved to {txt_file_path}.')
