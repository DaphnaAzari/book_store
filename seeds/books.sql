CREATE TABLE IF NOT EXISTS books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  author VARCHAR(255),
  release_date VARCHAR(255)
);

TRUNCATE table books;

INSERT INTO books (title, author, release_date) VALUES ('The Gruffalo', 'Julia Donaldson', '23/03/1999');
INSERT INTO books (title, author, release_date) VALUES ('Ada Twist, Scientist', 'Andrea Beaty', '6/09/2016');
INSERT INTO books (title, author, release_date) VALUES ('The Girl Who Drank the Moon', 'Kelly Barnhill', '9/08/2016');
INSERT INTO books (title, author, release_date) VALUES ('Dragons in a Bag', 'Zetta Elliott', '23/10/2018');
