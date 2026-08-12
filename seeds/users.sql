CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL
);

TRUNCATE table users;

-- INSERT INTO books (title, author, release_date) VALUES ('The Gruffalo', 'Julia Donaldson', '23/03/1999');
-- INSERT INTO books (title, author, release_date) VALUES ('Ada Twist, Scientist', 'Andrea Beaty', '6/09/2016');
-- INSERT INTO books (title, author, release_date) VALUES ('The Girl Who Drank the Moon', 'Kelly Barnhill', '9/08/2016');
-- INSERT INTO books (title, author, release_date) VALUES ('Dragons in a Bag', 'Zetta Elliott', '23/10/2018');
