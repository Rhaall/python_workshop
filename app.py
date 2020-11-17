from flask import Flask
from Models.User import User
from database.database import db_session
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)
sentence = 'At eight o\'clock on Thursday morning ... Arthur didn\'t feel very good.'

@app.route('/')
def home():
    sid = SentimentIntensityAnalyzer()

    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = nltk.word_tokenize(sentence)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

    # print(nouns)
    return sid.polarity_scores(sentence)

@app.route('/user')
def user():
    # test = User.query.all()
    # test = User.query.filter_by(username='michel_dupont').first()
    # test = database.db.session.query(User).filter(User.username == 'michel_dupont')

    # print(test)

    return 'test'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()
