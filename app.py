from flask import Flask, request
from Models.User import User
from Models.Event import Event
from Models.Keyword import Keyword
from Models.KeywordByUser import KeywordByUser
from Models.Location import Location
from database.database import db_session, get_data
from googletrans import Translator, constants
from pprint import pprint
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)
sentence = 'i love sports, this sensation of exaltation in nature is truly blessed'


# sentence = 'i hate sports and nature !'

@app.route('/')
def home():
    # translator = Translator()
    # translation = translator.translate("Bonjour à tous")
    # print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    return ""


@app.route('/eventUser/<id>', methods=['POST'])
def show_event(id):
    user = User.query.filter_by(id=id).first()
    if hasattr(user, 'id') == False:
        return 'user does not exist'

    posts = get_data()
    if str(user.id) not in posts:
        return "no post for this user"

    for post in posts[str(user.id)]:
        post = posts[str(user.id)][post]

        sid = SentimentIntensityAnalyzer()
        values = sid.polarity_scores(post)

        is_noun = lambda pos: pos[:2] == 'NN'
        tokenized = nltk.word_tokenize(post)
        nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

        for noun in nouns:
            keyword = Keyword.query.filter_by(label=noun).first()
            if hasattr(keyword, 'id'):
                insertOrUpdateKeywordByUsers(keyword, values, id)

    best_keyword_id = getBestKeywordId(id)
    keyword = Keyword.query.filter_by(id=best_keyword_id).first()
    if not hasattr(keyword, 'event_id'):
        return 'no keyword found for this user'

    event = Event.query.filter_by(id=keyword.event_id).first()
    if not request.json or 'location' not in request.json:
        return "location is missing"

    location = Location.query.filter_by(city=request.json['location']).first()
    response = "Location does not exist"
    if hasattr(location, 'id'):
        event = Event.query.filter_by(id=keyword.event_id, location_id=location.id).first()
        response = getEventJson(event, location) if (hasattr(event, 'label')) else "no event found"

    return response


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
    db_session.commit()


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
    events = {}
    if request.json and 'location' in request.json:
        location_id = request.json['location']
        location = Location.query.filter_by(city=location_id).first()

        if hasattr(location, 'id'):
            query = Event.query.filter_by(location_id=location.id)
            for event in query:
                events[event.id] = getEventJson(event, location)

    return events


def getEventJson(event, location):
    return {
        'event': {'label': event.label, 'description': event.description, 'picture': event.picture},
        'location': location.city
    }


@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    usr = User.query.filter_by(username=username).first()
    return {"id": usr.id}


@app.route('/me/<id>', methods=['POST'])
def user(id):
    user = User.query.filter_by(id=id).first()
    return {'username': user.username, 'firstname': user.firstname, 'lastname': user.lastname}


@app.route('/bind/user/<id>', methods=['POST'])
def bind(id):
    if request.json and 'social_network' in request.json:
        return {
            "user": id,
            "social_network": request.json['social_network']
        }
    else:
        return "data social_network is missing"


@app.route('/unbind/user/<id>', methods=['POST'])
def unbind(id):
    if request.json and 'social_network' in request.json:
        return {
            "user": id,
            "social_network": request.json['social_network']
        }
    else:
        return "data social_network is missing"


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()
