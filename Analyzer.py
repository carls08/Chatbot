from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
x= "It was horrible experience"

sid = SentimentIntensityAnalyzer()
resultados = sid.polarity_scores(x)

print(resultados)
