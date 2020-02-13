from flask import Flask, render_template

app = Flask(__name__)


books_data = [
	{'id':0, 'title':'Lord of the Rings', 'author':'J.R. Tolkien', 'category':'Fantasy', 'year': 1968},
	{'id':1, 'title':'Pet Semetary', 'author':'Stephen King', 'category':'Horror', 'year': 1979},
	{'id':2, 'title':'War and Peace', 'author':'Leo Tolstoy', 'category':'Fiction', 'year': 1962}
]
 

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/books')
def books():
    return render_template('books.html', books=books_data)


@app.route('/book/view/<int:id>')
def book_view(id):
    return render_template('book-view.html', book=books_data[id])


@app.route('/members')
def members():
    return render_template('members.html')

@app.route('/loans')
def loans():
    return render_template('loans.html')


@app.route('/reports')
def reports():
    return render_template('reports.html')


