from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow.exceptions import ValidationError
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema 

app = Flask(__name__)
api = Api(app)
 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
 
db = SQLAlchemy(app)
ma = Marshmallow(app)
 
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(50))
    year = db.Column(db.Integer)
 
    def __repr__(self):
        return f"<Book {self.title} from {self.publisher}>"

''' 
class BookSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    title = ma.String(required=True)
    publisher = ma.String()
    year = ma.Integer()
'''

class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book

book_schema = BookSchema()
books_schema = BookSchema(many=True)
 
class BookResource(Resource):
    def get(self, id=None):
        if not id:
            books = Book.query.all()
            return books_schema.dump(books)
        else:
            book = Book.query.get_or_404(id)
            return book_schema.dump(book)
    def post(self):
        json = request.get_json()
        try:
            book = book_schema.load(json, session=db.session)
            #book = Book(**data)
            db.session.add(book)
            db.session.commit()
            return {
                "message": "success"
            }, 201
        except ValidationError as err:
            return {
                "errors": err.messages
            }, 400
 
api.add_resource(BookResource, "/book", "/book/<id>")
 
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
