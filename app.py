from flask import Flask, request
from Models.User import User
from Models.Event import Event
from Models.Keyword import Keyword
from Models.KeywordByUser import KeywordByUser
from database.database import db_session
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)
# sentence = 'i love sports, this sensation of exaltation in nature is truly blessed'
sentence = 'i hate sports and nature !'

@app.route('/')
def home():
    sid = SentimentIntensityAnalyzer()

    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = nltk.word_tokenize(sentence)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

    # test = User.query.all()

    # print(nouns)
    return sid.polarity_scores(sentence)


@app.route('/eventUser/<id>')
def ChooseEvent(id):
    user = User.query.filter_by(id=id).first()
    if hasattr(user, 'id') == False:
        return 'L\'utilisateur n\'existe pas !'

    sid = SentimentIntensityAnalyzer()
    values = sid.polarity_scores(sentence)

    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = nltk.word_tokenize(sentence)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

    for noun in nouns:
        keyword = Keyword.query.filter_by(label=noun).first()
        if hasattr(keyword, 'id'):
            user_keyword = KeywordByUser.query.filter_by(id_keyword=keyword.id, id_user=user.id).first()
            if hasattr(user_keyword, 'id'):
                count = user_keyword.count
                user_keyword.pos_rate = ((user_keyword.pos_rate * count) + values['pos']) / (count + 1)
                user_keyword.neg_rate = ((user_keyword.neg_rate * count) + values['neg']) / (count + 1)
                user_keyword.neutral_rate = ((user_keyword.neutral_rate * count) + values['neu']) / (count + 1)
                user_keyword.count = count + 1
            else:
                KeywordByUsers = KeywordByUser(
                    id_user=id, id_keyword=keyword.id, pos_rate=values['pos'],
                    neg_rate=values['neg'], neutral_rate=values['neu'], count=1
                )
                db_session.add(KeywordByUsers)

    db_session.commit()
    return ""

@app.route('/events', methods=['POST'])
def events():
    location_id = request.json['location']
    query = Event.query.filter_by(location_id=location_id)
    events = {}
    for event in query:
        events[event.id] = event.label

    return events

@app.route('/me/<id>')
def user(id):
    user = User.query.filter_by(id=id).first()
    return {'username': user.username, 'firstname': user.firstname, 'lastname': user.lastname}

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
