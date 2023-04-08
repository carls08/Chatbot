import re
import bs4 as bs
import urllib.request
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import bs4
import urllib.request
from bs4 import BeautifulSoup
import urllib.request
from inscriptis import get_text
from googletrans import Translator

##Scrapear
enlace = input(f'Ingrese el link de la pagina\n ')
minLetters = 250
html =urllib.request.urlopen(enlace).read().decode('utf-8')
text = get_text(html)
article_text =  text
article_text = article_text.replace("[ edit]","")


from nltk import word_tokenize,sent_tokenize
##Elimina caracteres especiales y espacios
article_text = re.sub(r'\[[0-9]*\]',' ', article_text)
article_text = re.sub(r'\s+',' ',article_text)

formatted_article_text = re.sub('[^a-zA-Z]',' ',article_text)
formatted_article_text= re.sub(r'\s+',' ',formatted_article_text)

##tokenizacion
sentence_list =nltk.sent_tokenize(article_text)

##Separa palabra y frecuencia
stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word]+=1
        
maximun_frequency = max(word_frequencies.values())
for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximun_frequency)
    
    
## frases que se repiten
sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < minLetters:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else :
                    sentence_scores[sent] += word_frequencies[word]

##resumen

opc= input('¿Desea traducir el resumen? y/n \n')
import heapq  
summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
summary = ' '.join(summary_sentences)  
if(opc=='n'):
   print(summary)
else:
   
    translator = Translator()
    translate = translator.translate(summary, src="en", dest="es")
    print("***************************TRADUCCIÓN*******************************")
    print(translate.text)