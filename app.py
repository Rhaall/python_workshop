from flask import Flask
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)
sentence = 'At eight o\'clock on Thursday morning ... Arthur didn\'t feel very good.'

@app.route('/')
def hello_world():
    sid = SentimentIntensityAnalyzer()

    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = nltk.word_tokenize(sentence)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

    # print(nouns)
    return sid.polarity_scores(sentence)


if __name__ == '__main__':
    app.run()
