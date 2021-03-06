create table members (
	id INTEGER primary key autoincrement,
	first_name TEXT not null,
	last_name TEXT not null,
	role TEXT,
	phone TEXT,
	email TEXT,
	avatar TEXT DEFAULT 'avatar.png'
);

create table books (
	id INTEGER primary key autoincrement,
	title TEXT not null,
	isbn TEXT UNIQUE,
	author TEXT not null,
	description TEXT,
	year_published INTEGER,
	copies INTEGER DEFAULT 1,
	category TEXT DEFAULT 'uknown',
	cover TEXT DEFAULT 'cover.png'
);

create table loans (
	id INTEGER primary key autoincrement,
	checkout_date TEXT default CURRENT_DATE,
	checkin_date TEXT,
	member_id INTEGER not null,
	book_id INTEGER not null,

	foreign key(member_id) references members(id),
	foreign key(book_id) references books(id)
);


INSERT INTO members (first_name, last_name, role)
VALUES
	('Teo', 'Bous', 'Teacher'),
	('George', 'Voutsinos', 'Student'),
	('Toni', 'Roussos', 'Student'),
	('Fivos', 'Kaintas', 'Student'),
	('Armanto', 'Metko', 'Student'),
	('Pan', 'Hypermahos', 'Student'),
	('Chris', 'Bill', 'Teacher'),
	('Peterl', 'Lazarinos', 'Student');



INSERT INTO books (title, isbn, author, description, year_published, copies, category, cover)
VALUES
	('Lord of the Rings', '9994440041', 'J.R. Tolkien', 'some description', 1968, 1, 'Fantasy', 'lord-of-the-rings.jpg'),
	('Pet Semetary', '9994440054', 'Stephen King', 'some description', 1979, 1, 'Horror', 'pet-sematary.jpg'),
 	('War and Peace', '9994440042', 'Leo Tolstoy', 'some description', 1962, 2, 'Fiction', 'war-and-peach.jpg'),
 	('The C Programming Language', '0131103628', 'Dennis M. Ritchie', 'some description', 1978, 3, 'Technology', 'the-c-programming-language.jpg'),
 	('At the Mountains of Madness', '9894340044', 'H.P. Lovecraft', 'some description', 2010, 2, 'Horror', 'at-the-mountain-of-madness.jpg');

 INSERT INTO loans (checkout_date, checkin_date, member_id, book_id)
 VALUES
 	('2020-01-12', '2020-01-19', 1, 3),
 	('2020-01-22', '2020-01-30', 1, 3),
 	('2019-12-01', '2019-12-19', 2, 1),
 	('2020-01-12', '2020-01-19', 3, 2),
 	('2020-01-12', NULL, 4, 3),
 	('2020-01-12', '2020-01-19', 4, 4),
 	('2020-01-12', '2020-01-19', 4, 5),
 	('2020-01-12', NULL, 5, 4),
 	('2020-01-12', NULL, 6, 3),
 	('2020-01-12', '2020-01-19', 7, 2),
 	('2020-01-12', NULL, 8, 2),
 	('2020-01-12', '2020-01-19', 8, 1);
