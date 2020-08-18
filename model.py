# pip install pyresparser
# python -m nltk.downloader words
# python -m spacy download en_core_web_sm


from pyresparser import ResumeParser
import os
import json
import spacy

dat_file_storage = './dat_files'

for root, dirs, files in os.walk("./pdf_files", topdown=False):
    for name in files:
        print('Accessing File: '+name)
        filename = (os.path.join(root, name))
        if filename.endswith('.pdf'):
            data=ResumeParser(filename).get_extracted_data()
            
            file_path = os.path.join(dat_file_storage, name)
            
            with open(file_path[:-4]+'.dat', 'w') as file:
                    file.write(json.dumps(data))





# SUMMARY

from gensim.parsing.preprocessing import remove_stopwords

summary=remove_stopwords(data)
        
print(summary)