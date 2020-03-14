import os
from flask import Flask, render_template, g, request, redirect, url_for
from database import connect_db, get_db

app = Flask(__name__)

app.config['COVERS_UPLOAD_FOLDER'] = 'static/uploads/covers'
app.config['AVATARS_UPLOAD_FOLDER'] = 'static/uploads/avatars'


# Για να κλείνει αυτόματα η βάση δεδομέων
@app.teardown_appcontext
def close_db(error):
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/books')
def books():
	db = get_db()
	
	query = "SELECT * FROM books"
	cur = db.execute(query)
	results = cur.fetchall()
	
	return render_template('books.html', books=results)


@app.route('/book/view/<int:id>')
def book_view(id):
	db = get_db()
	query = "SELECT * FROM BOOKS WHERE id = ?"
	cur = db.execute(query, [id])
	result=cur.fetchone()

	return render_template('book-view.html', book=result)

@app.route('/book/add', methods = ['GET', 'POST'])
def book_add():
	db = get_db()
	if request.method == 'POST':
		title = request.form['title']
		description = request.form['description']
		author = request.form['author']
		isbn = request.form['isbn']
		category = request.form['category']
		year = request.form['year']
		copies = request.form['copies']

		if request.files:
			cover = request.files['cover']
			abs_path = os.path.abspath(app.config['COVERS_UPLOAD_FOLDER'])
			cover.save(os.path.join(abs_path, cover.filename))


		query = 'insert into books (title, description, author, isbn, category, year_published, copies, cover) values (?, ?, ?, ?, ?, ?, ?, ?)'
		db.execute(query, [title, description, author, isbn, category, year, copies, cover.filename])
		db.commit()

		print("submited", cover.filename)
		return redirect(url_for('books'))


	return render_template('book-add.html')


@app.route('/members')
def members():
	db = get_db()

	query = "SELECT * FROM members"
	cur = db.execute(query)
	results = cur.fetchall()

	return render_template('members.html', members=results)


@app.route('/member/view/<int:id>')
def member_view(id):
	db = get_db()
	query = "SELECT * FROM members WHERE id = ?"
	cur = db.execute(query, [id])
	result=cur.fetchone()

	return render_template('member-view.html', member=result)

@app.route('/loans')
def loans():
	db = get_db()

	query = """
				SELECT loans.id AS id, checkout_date, checkin_date, title, first_name, last_name
				FROM loans
				JOIN books ON loans.book_id = books.id
				JOIN members ON loans.member_id = members.id;
			"""
	cur = db.execute(query)
	results = cur.fetchall()

	return render_template('loans.html', loans=results)


@app.route('/reports')
def reports():
    return render_template('reports.html')


