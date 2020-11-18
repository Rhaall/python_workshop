from flask import Flask, request
from Models.User import User
from Models.Event import Event
from Models.Keyword import Keyword
from Models.KeywordByUser import KeywordByUser
from database.database import db_session
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)
sentence = 'i love sports, this sensation of exaltation in nature is truly blessed'
# sentence = 'i hate sports and nature !'

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
def show_event(id):
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
            insertOrUpdateKeywordByUsers(keyword, values, id)

    db_session.commit()
    best_keyword_id = getBestKeywordId(id)
    keyword = Keyword.query.filter_by(id=best_keyword_id).first()
    if not hasattr(keyword, 'event_id'):
        return 'Aucun mot clé trouvé pour cet utilisateur'

    event = Event.query.filter_by(id=keyword.event_id).first()

    return event.label if (hasattr(event, 'label')) else ""

def insertOrUpdateKeywordByUsers(keyword, values, user_id):
    user_keyword = KeywordByUser.query.filter_by(id_keyword=keyword.id, id_user=user_id).first()
    if hasattr(user_keyword, 'id'):
        count = user_keyword.count
        user_keyword.pos_rate = ((user_keyword.pos_rate * count) + values['pos']) / (count + 1)
        user_keyword.neg_rate = ((user_keyword.neg_rate * count) + values['neg']) / (count + 1)
        user_keyword.neutral_rate = ((user_keyword.neutral_rate * count) + values['neu']) / (count + 1)
        user_keyword.count = count + 1
    else:
        user_keyword = KeywordByUser(
            id_user=user_id, id_keyword=keyword.id, pos_rate=values['pos'],
            neg_rate=values['neg'], neutral_rate=values['neu'], count=1
        )
        db_session.add(user_keyword)


def getBestKeywordId(id):
    listofwordbyuser = KeywordByUser.query.filter_by(id_user=id)
    max = -150
    keyword_id = -1
    for word_by_user in listofwordbyuser:
        current_value = word_by_user.pos_rate - ((word_by_user.neutral_rate + word_by_user.neg_rate * 2) / 3)
        if current_value > max:
            max = current_value
            keyword_id = word_by_user.id_keyword
    return keyword_id

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
