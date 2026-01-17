from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.exceptions import ValidationError
 
app = Flask(__name__)
api = Api(app)
 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
 
db = SQLAlchemy(app)
ma = Marshmallow(app)
 
class Publisher(db.Model):
  __tablename__ = "publishers"
 
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(40), nullable=False, unique=True)
  city = db.Column(db.String(30))
 
  books = db.relationship("Book", back_populates="publisher")

class BookAuthor(db.Model):
    __tablename__ = "book_authors"
     
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"), primary_key=True)

    book = db.relationship("Book", back_populates="authors") 
    author = db.relationship("Author", back_populates="books")

class Author(db.Model):
    __tablename__ = "authors"
     
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
     
    books = db.relationship("BookAuthor", back_populates="author")    
 
class Book(db.Model):
  __tablename__ = "books"
 
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String(200), nullable=False)
  publisher_id = db.Column(db.Integer, db.ForeignKey("publishers.id"))
  year = db.Column(db.Integer)
 
  publisher = db.relationship("Publisher", back_populates="books")
  authors = db.relationship("BookAuthor", back_populates="book")
 
class PublisherSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = Publisher
    load_instance = True
 
publisher_schema = PublisherSchema()
publishers_schema = PublisherSchema(many=True)

class AuthorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        load_instance = True

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

class BookAuthorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = BookAuthor
        load_instance = True
        include_fk = True

book_author_schema = BookAuthorSchema()
book_authors_schema = BookAuthorSchema(many=True)
 
class BookSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = Book
    load_instance = True
    include_fk = True
 
book_schema = BookSchema()
books_schema = BookSchema(many=True)
 
class PublisherResource(Resource):
  def get(self, id=None):
    if not id:
      publishers = Publisher.query.all()
      return publishers_schema.dump(publishers)
    else:
      publisher = Publisher.query.get_or_404(id)
      return publisher_schema.dump(publisher)
 
  def post(self):
    data = request.get_json()
    try:
      publisher = publisher_schema.load(data, session=db.session)
      db.session.add(publisher)
      db.session.commit()
      return publisher_schema.dump(publisher), 201
    except ValidationError as err:
      return {"errors": err.messages}, 400
 
  def put(self, id):
    publisher = Publisher.query.get_or_404(id)
    data = request.get_json()
    try:
      inpublisher = publisher_schema.load(data, session=db.session)
      publisher.name = inpublisher.name
      publisher.city = inpublisher.city
      db.session.commit()
      return publisher_schema.dump(publisher)
    except ValidationError as err:
      return {"errors": err.messages}, 400
 
  def patch(self, id):
    publisher = Publisher.query.get_or_404(id)
    data = request.get_json()
    publisher.title = data.get('name', publisher.name)
    publisher.publisher = data.get('city', publisher.city)
    db.session.commit()
    return publisher_schema.dump(publisher)
 
  def delete(self, id):
    publisher = Publisher.query.get_or_404(id)
    db.session.delete(publisher)
    db.session.commit()
    return {"message": "Publisher deleted successfully"}
  
class BookAuthorResource(Resource):
  def get(self, book_id=None, author_id=None):
    if book_id and author_id:
      book_author = BookAuthor.query.get_or_404((book_id, author_id))
      return book_author_schema.dump(book_author)
    else:
      book_authors = BookAuthor.query.all()
      return book_authors_schema.dump(book_authors)
 
  def post(self):
    data = request.get_json()
    try:
      book_author = book_author_schema.load(data, session=db.session)
      db.session.add(book_author)
      db.session.commit()
      return book_author_schema.dump(book_author), 201
    except ValidationError as err:
      return {"errors": err.messages}, 400

  def put(self, id):
    bookauthor = BookAuthor.query.get_or_404(id)
    data = request.get_json()
    try:
      inbookauthor = book_author_schema.load(data, session=db.session)
      bookauthor.name = inbookauthor.name
      bookauthor.city = inbookauthor.city
      db.session.commit()
      return book_author_schema.dump(bookauthor)
    except ValidationError as err:
      return {"errors": err.messages}, 400
 
  def patch(self, id):
    bookauthor = BookAuthor.query.get_or_404(id)
    data = request.get_json()
    bookauthor.title = data.get('name', bookauthor.name)
    bookauthor.bookauthor = data.get('city', bookauthor.city)
    db.session.commit()
    return book_author_schema.dump(bookauthor)     
 
  def delete(self, book_id, author_id):
    book_author = BookAuthor.query.get_or_404((book_id, author_id))
    db.session.delete(book_author)
    db.session.commit()
    return {"message": "Book-Author association deleted successfully"} 

class AuthorResource(Resource):
  def get(self, id=None):
    if not id:
      authors = Author.query.all()
      return authors_schema.dump(authors)
    else:
      author = Author.query.get_or_404(id)
      return author_schema.dump(author)
 
  def post(self):
    data = request.get_json()
    try:
      author = author_schema.load(data, session=db.session)
      db.session.add(author)
      db.session.commit()
      return author_schema.dump(author), 201
    except ValidationError as err:
      return {"errors": err.messages}, 400
 
  def put(self, id):
    author = Author.query.get_or_404(id)
    data = request.get_json()
    try:
      inauthor = author_schema.load(data, session=db.session)
      author.name = inauthor.name
      db.session.commit()
      return author_schema.dump(author)
    except ValidationError as err:
      return {"errors": err.messages}, 400
 
  def patch(self, id):
    author = Author.query.get_or_404(id)
    data = request.get_json()
    author.name = data.get('name', author.name)
    db.session.commit()
    return author_schema.dump(author)
 
  def delete(self, id):
    author = Author.query.get_or_404(id)
    db.session.delete(author)
    db.session.commit()
    return {"message": "Author deleted successfully"}   
  
class BookResource(Resource):
  def get(self, id=None):
    if not id:
      books = Book.query.all()
      return books_schema.dump(books)
    else:
      book = Book.query.get_or_404(id)
      return book_schema.dump(book)
 
  def post(self):
    data = request.get_json()
    try:
      book = book_schema.load(data, session=db.session)
      db.session.add(book)
      db.session.commit()
      return book_schema.dump(book), 201
    except ValidationError as err:
      return {"errors": err.messages}, 400
 
  def put(self, id):
    book = Book.query.get_or_404(id)
    data = request.get_json()
    try:
      inbook = book_schema.load(data, session=db.session)
      book.title = inbook.title
      book.publisher_id = inbook.publisher_id
      book.year = inbook.year
      db.session.commit()
      return book_schema.dump(book)
    except ValidationError as err:
      return {"errors": err.messages}, 400
 
  def patch(self, id):
    book = Book.query.get_or_404(id)
    data = request.get_json()
    book.title = data.get('title', book.title)
    book.publisher_id = data.get('publisher_id', book.publisher_id)
    book.year = data.get('year', book.year)
    db.session.commit()
    return book_schema.dump(book)
 
  def delete(self, id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return {"message": "Book deleted successfully"}
 
class BookListByPublisher(Resource):
  def get(self, id):
    publisher = Publisher.query.get_or_404(id)
    books = publisher.books
    return books_schema.dump(books)
 
api.add_resource(PublisherResource, "/publisher", "/publisher/<id>")
api.add_resource(BookResource, "/book", "/book/<id>")
api.add_resource(BookListByPublisher, "/book/publisher/<id>")
api.add_resource(AuthorResource, "/author", "/author/<id>")
api.add_resource(BookAuthorResource, "/book_author", "/book_author/<int:book_id>/<int:author_id>")
 
if __name__ == "__main__":
  with app.app_context():
    db.create_all()
  app.run(debug=True)