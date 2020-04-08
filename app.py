from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

api = Flask(__name__)

api.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:admin@127.0.0.1/amex"
db = SQLAlchemy(api)

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"Student('{self.name}')"
        
@api.route('/companies', methods=['GET'])
def get_companies():
    data = Student(name="Tarun")
    db.session.add(data)
    db.session.commit()
    res = Student.query.all()
    return json.dumps(res)

if __name__ == '__main__':
    api.run()