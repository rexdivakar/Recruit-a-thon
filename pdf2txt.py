import PyPDF2
from nltk.tokenize import sent_tokenize
import os
import shutil

txt_file_storage = './txt_files'

for root, dirs, files in os.walk("./pdf_files", topdown=False):
    for name in files:
        print('Accessing File: '+name)
        filename = (os.path.join(root, name))
        if filename.endswith('.pdf'):
                pdfFileObj = open(filename, 'rb')

                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

                num_pages = pdfReader.numPages
                count = 0
                text = ""
                # The while loop will read each page.
                while count < num_pages:
                    pageObj = pdfReader.getPage(count)
                    count += 1
                    text += pageObj.extractText()

                tokens = sent_tokenize(text)

                op = ' '.join(tokens).replace('\n', '')

                file_path = os.path.join(txt_file_storage, name)
                
                f = open(file_path[:-3]+'.txt', 'w', encoding='utf-8')
                for i in op:
                    f.writelines(i)

print('Finished Conversion')