/* ############ INSERTION ############# */

INSERT INTO "user"
VALUES (DEFAULT, 'michel_dupont', 'Michel', 'Dupont');

INSERT INTO location
VALUES (DEFAULT, 'Arles'),
       (DEFAULT, 'Montpellier'),
       (DEFAULT, 'Avignon');


INSERT INTO event
VALUES (DEFAULT, 'Rap Concert', 'Come and attend Eminem''s last concert for his album The Marshall Mathers LP', 'image.workshop.tsukiru.com/rap.jpg', 2),
       (DEFAULT, 'Rock Concert', 'System of a Down is back with two new unreleased tracks', 'image.workshop.tsukiru.com/rock.jpg', 2),
       (DEFAULT, 'Tree climbing', 'Want to spend a moment with friends close to nature, come and try the tree climbing', 'image.workshop.tsukiru.com/accrobranche.jpg', 1),
       (DEFAULT, 'Tennis tournaments', 'A fun inter-generational tournament and a thrilling afternoon guaranteed by this tennis tournament', 'image.workshop.tsukiru.com/tennis.jpg', 3),
       (DEFAULT, 'Fitness trail', 'Uber eats bringing you too much regret? a place to absolve your sins', 'image.workshop.tsukiru.com/parcours.jpg', 1),
       (DEFAULT, 'Cinematographic projection', 'Christopher Nolan''s new film is already available in your nearest cinema', 'image.workshop.tsukiru.com/cinema.jpg', 1),
       (DEFAULT, 'Exposure', 'On the occasion of its last provocative work, the city offers a look back on the career of the street artist Banksy', 'image.workshop.tsukiru.com/exposition.jpg', 2);


INSERT INTO keyword
VALUES (DEFAULT, 'BOOBA', 1),
       (DEFAULT, 'street', 1),
       (DEFAULT, 'gang', 1),
       (DEFAULT, 'tennis', 4),
       (DEFAULT, 'racket', 4),
       (DEFAULT, 'nature', 5),
       (DEFAULT, 'effort', 3),
       (DEFAULT, 'pleasure', 3),
       (DEFAULT, 'duel', 4),
       (DEFAULT, 'painting', 7),
       (DEFAULT, 'artist', 7),
       (DEFAULT, 'discovery', 6),
       (DEFAULT, 'director', 6),
       (DEFAULT, 'match', 4),
       (DEFAULT, 'confrontation', 4),
       (DEFAULT, 'equipment', 3),
       (DEFAULT, 'series', 6),
       (DEFAULT, 'movie', 6),
       (DEFAULT, 'projection', 6),
       (DEFAULT, 'book', 7),
       (DEFAULT, 'author', 6);