from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields
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
 
class Author(db.Model):
  __tablename__ = "authors"
 
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(40), nullable=False)
 
  books = db.relationship("Book", secondary="book_authors", back_populates="authors")
 
class Book(db.Model):
  __tablename__ = "books"
 
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String(200), nullable=False)
  publisher_id = db.Column(db.Integer, db.ForeignKey("publishers.id"))
  year = db.Column(db.Integer)
 
  publisher = db.relationship("Publisher", back_populates="books")
  authors = db.relationship("Author", secondary="book_authors", back_populates="books")
 
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
 
class BookLoaderSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = Book
    include_fk = True
 
  author_ids = ma.List(ma.Integer)
 
book_loader_schema = BookLoaderSchema()
 
class BookDumperSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = Book
    include_relationship = True
 
  publisher = fields.Nested(PublisherSchema, dump_only=True)
  authors = fields.Nested(AuthorSchema, many=True, dump_only=True)
 
book_dumper_schema = BookDumperSchema()
books_dumper_schema = BookDumperSchema(many=True)
 
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
    publisher.name = data.get('name', publisher.name)
    publisher.city = data.get('city', publisher.city)
    db.session.commit()
    return publisher_schema.dump(publisher)
 
  def delete(self, id):
    publisher = Publisher.query.get_or_404(id)
    db.session.delete(publisher)
    db.session.commit()
    return {"message": "Publisher deleted successfully"}
 
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
      return books_dumper_schema.dump(books)
    else:
      book = Book.query.get_or_404(id)
      return book_dumper_schema.dump(book)
 
  def post(self):
    data = request.get_json()
    try:
      loaded = book_loader_schema.load(data, session=db.session)
      publisher = Publisher.query.get_or_404(loaded["publisher_id"])
      authors = [Author.query.get_or_404(id) for id in loaded["author_ids"]]
 
      book = Book(title=loaded["title"], year=loaded["year"],
                  publisher=publisher, authors=authors)
      db.session.add(book)
      db.session.commit()
      return book_dumper_schema.dump(book), 201
    except ValidationError as err:
      return {"errors": err.messages}, 400
 
  def put(self, id):
    book = Book.query.get_or_404(id)
    data = request.get_json()
    try:
      loaded = book_loader_schema.load(data, session=db.session)
      book.title = loaded["title"]
      book.publisher = Publisher.query.get_or_404(loaded["publisher_id"])
      book.year = loaded["year"]
      book.authors.clear()
      book.authors.extend([Author.query.get_or_404(id) for id in loaded["author_ids"]])
      db.session.commit()
      return book_dumper_schema.dump(book)
    except ValidationError as err:
      return {"errors": err.messages}, 400
 
  def patch(self, id):
    book = Book.query.get_or_404(id)
    data = request.get_json()
    book.title = data.get('title', book.title)
    book.publisher_id = data.get('publisher_id', book.publisher_id)
    book.year = data.get('year', book.year)
    if 'author_ids' in data:
      book.authors.clear()
      book.authors.extend([Author.query.get_or_404(id) for id in data["author_ids"]])
    db.session.commit()
    return book_dumper_schema.dump(book)
 
  def delete(self, id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return {"message": "Book deleted successfully"}
 
class BookListByPublisher(Resource):
  def get(self, id):
    publisher = Publisher.query.get_or_404(id)
    books = publisher.books
    return books_dumper_schema.dump(books)
  
class BookListByAuthor(Resource):
  def get(self, id):
    author = Author.query.get_or_404(id)
    books = author.books
    return books_dumper_schema.dump(books)
 
api.add_resource(PublisherResource, "/publisher", "/publisher/<id>")
api.add_resource(AuthorResource, "/author", "/author/<id>")
api.add_resource(BookResource, "/book", "/book/<id>")
api.add_resource(BookListByPublisher, "/book/publisher/<id>")
api.add_resource(BookListByAuthor, "/book/author/<id>")
 
if __name__ == "__main__":
  with app.app_context():
    db.create_all()
  app.run(debug=True)