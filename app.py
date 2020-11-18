from flask import Flask, jsonify, request
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

    # test = User.query.all()

    # print(nouns)
    return sid.polarity_scores(sentence)

@app.route('/me/<id>')
def user(id):
    test = User.query.filter_by(id=id).first()

    return {'username': test.username, 'firstname': test.firstname, 'lastname': test.lastname}

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    usr = User.query.filter_by(username=username).first()
    return {"id" : usr.id}

@app.route('/bind/user/<idUser>', methods=['POST'])
def bind(idUser):
    return {
        "user":idUser,
        "social_network": request.json['social_network']
    }

@app.route('/unbind/user/<idUser>', methods=['POST'])
def unbind(idUser):
    return {
        "user":idUser,
        "social_network": request.json['social_network']
    }

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()
