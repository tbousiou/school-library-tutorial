from flask import Flask, render_template, g
from database import connect_db, get_db

app = Flask(__name__)



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
	
	query = "SELECT * FROM books";
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


@app.route('/members')
def members():
    return render_template('members.html')

@app.route('/loans')
def loans():
    return render_template('loans.html')


@app.route('/reports')
def reports():
    return render_template('reports.html')


