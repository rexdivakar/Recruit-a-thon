import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt') # if necessary...

data='"Mining", "Mysql", "Security", "Windows", "Information technology", "C++", "Python", "Keras", "Opencv", "Programming", "Database", "Machine learning", "Jupyter", "Pandas", "Javascript", "Algorithms", "Linux", "Js", "Nose", "Ubuntu", "Pytorch", "Java", "Php", "Testing", "R", "Numpy", "Matplotlib", "Content", "Pycharm", "Technical", "Social media", "Tensorflow", "Anaconda", "System", "Api", "Expenses", "Android"'

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

ip_data='python, data science, machine learning, keras'


print (cosine_sim(ip_data, data))