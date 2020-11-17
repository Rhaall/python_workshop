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
    keyword varchar(50)
);

CREATE TABLE events
(
    id INTEGER primary key,
    label varchar(50),
    id_localisation integer,
    FOREIGN KEY (id_localisation) REFERENCES localisation (id)
);
