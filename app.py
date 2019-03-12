from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Book

@app.route('/')
def hello():
    return "Hello"

@app.route('/add')
def add_book():
    name = request.args.get('name')
    author = request.args.get('author')
    publishdate = request.args.get('publishdate')

    try:
        book = Book(
            name=name,
            author=author,
            publishdate=publishdate
        )
        db.session.add(book)
        db.session.commit()
        return "Book adde. Book id : {}".format(book.id)
    except Exception as e:
        return (str(e))

@app.route('/books')
def getAllBooks():
    try:
        books = Book.query.all()
        return jsonify([e.serialize() for e in books])
    except Exception as e:
        return (str(e))

@app.route('/get/<id_>')
def get_by_id(id_):
    try:
        book = Book.query.filter_by(id=id_).first()
        return jsonify(book.serialize())
    except Exception as e:
        return (str(e))


@app.route('/add/form', methods=['GET', 'POST'])
def add_book_form():
    if request.method == 'POST':
        name = request.form.get('name')
        author = request.form.get('author')
        publishdate = request.form.get('publishdate')
        try:
            book = Book(
                name=name,
                author=author,
                publishdate=publishdate
            )
            db.session.add(book)
            db.session.commit()
            return "Book added. book id={}".format(book.id)
        except Exception as e:
            return (str(e))
    return render_template('addFile.html')

@app.route('/postjson',methods=['POST'])
def postJsonHandler():
    content=request.get_json()
    print(content)
    print(content['name'])
    print(content['author'])
    print(content['publishdate'])
    name = content['name']
    author = content['author']
    publishdate = content['publishdate']
    try:
        book = Book(name=name,author=author,publishdate=publishdate)
        db.session.add(book)
        db.session.commit()
        return "Book added. Book id={}".format(book.id)
    except Exception as e:
        return (str(e))

if __name__=='__main__':
    app.run(debug=True)