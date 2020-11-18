# Spare_Time Back-end

Front-end repository link : 
https://github.com/Sid-Djilali-Saiah/sparetime-frontend

## Used Technologies :
Python
PostgreSQL

## Dependencies :
PIP :
- Flask
- Flask-cors
- Alchemy
- NLTK :
  - Vader lexicon
  - Punkt
  - Averadged_perceptron_tagger
- Pathlib
- JSON
- Googletrans

## Routes Schema
+ POST /eventUser/<id>    Body: {location: city}    # Provides an event suggestion for a given user id
+ POST /events    Body: {location: city}    # Returns every events for a given location
+ POST /login   Body {username}   # Logging in a given user, returns its
+ POST /me/<id>   # Returns profile details for a given user id
+ POST /bind/user/<id>    Body:{social_network    # Links a given social network to a given user id
+ POST /unbind/user/<id>    Body:{social_network    # Unlinks a given social network to a given user id
