
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 

stop_words = set(stopwords.words('english'))

def clear_words(text):
    word_tokens = word_tokenize(text)
 
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    # print(filtered_sentence)
    return ' '.join(filtered_sentence)
 