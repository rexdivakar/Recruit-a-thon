# SUMMARY

with open('txt_files\Deepak Raghavendar CV..txt','r') as f:
    summary=f.read()

from gensim.parsing.preprocessing import remove_stopwords

summary=remove_stopwords(summary)
        
print(summary)