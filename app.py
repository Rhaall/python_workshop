from flask import Flask
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)


@app.route('/')
def hello_world():
    sentence = """At eight o'clock on Thursday morning ... 
    Arthur didn't feel very good."""
    sid = SentimentIntensityAnalyzer()
    return sid.polarity_scores(sentence)



if __name__ == '__main__':
    app.run()
