/* ############ CREATION ############# */
CREATE TABLE user
(
    id INTEGER primary key,
    lastname varchar(50),
    firstname varchar(50)
);

CREATE TABLE keyword
(
    id INTEGER primary key,
    keyword varchar(50)
);

CREATE TABLE key_word_by_user
(
    id INTEGER primary key,
    id_user integer,
    id_Keyword integer,
    pos_rate float,
    neg_rate float,
    neutral_rate float,
    count int,
    FOREIGN KEY (id_Keyword) REFERENCES keyword (id),
    FOREIGN KEY (id_user) REFERENCES user (id)
);

CREATE TABLE localisation
(
    id INTEGER primary key,
    city varchar(50)
);

CREATE TABLE event
(
    id INTEGER primary key,
    label varchar(50),
    id_localisation integer,
    FOREIGN KEY (id_localisation) REFERENCES localisation (id)
);

/* ############ INSERTION ############# */

INSERT into user VALUES
(null, "Michel","Dupont");

INSERT INTO localisation VALUES
(null, "Arles"),
(null, "Montpellier"),
(null, "Avignon");


INSERT INTO event VALUES
(null, "Concert de Rap de cité",2),
(null, "Concert de Rockeur bizarre",2),
(null, "Acrobranche",1),
(null, "Tournois de tennis",3),
(null, "Parcours santé avec les srabs",1),
(null, "Projection cinématographique",1),
(null, "Exposition",2);


INSERT INTO keyword VALUES 
(null, "BOOBA"),
(null, "street"),
(null,"gang"),
(null,"guitare"),
(null, "tennis"),
(null, "raquette"),
(null, "nature"),
(null, "effort"),
(null, "plaisir"),
(null, "duel"),
(null, "peinture"),
(null, "artiste"),
(null, "découverte"),
(null, "réalisateur"),
(null, "match"),
(null, "affrontement"),
(null, "equipement"),
(null, "série"),
(null, "film"),
(null, "projection"),
(null, "livre"),
(null, "auteur");