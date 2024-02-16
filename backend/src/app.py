from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ
import csv


# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
# create the extension
db = SQLAlchemy(app)

class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    comment = db.Column(db.String(500), nullable=True)
    case_id = db.Column(db.Integer, nullable=False)
    #cases = db.relationship('Case', secondary = 'case_location', back_populates = 'location')

class Case(db.Model):
    __tablename__ = 'cases'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)

class case_location(db.Model):
    __tablename__ = 'case_location'

    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, nullable=False)
    locations_id = db.Column(db.Integer, nullable=False)


#case_location = db.Table(
#  'case_location',
#  db.Column('case_id', db.Integer, db.ForeignKey('case.id')),
#  db.Column('location_id', db.Integer, db.ForeignKey('location.id'))
#)

class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    department = db.Column(db.String(200), nullable=False)

    def __init__(self, name, department):
        self.name = name
        self.department = department
    

db.create_all()

#create a test route
@app.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'qsgszsdg'}), 200)

@app.route('/populate')
def populate():
  with open('data.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        tab = row[0].split(';')
        city = City(tab[9], tab[4])
        with app.app_context():
            db.session.add(city)
            db.session.commit()
    return make_response(jsonify({'message': 'db populated'}), 201)
        

# create a case
@app.route('/create_case', methods=['POST'])
def create_case():
  #app.logger.info("request : ", request)
  data = request.json
  new_case = Case(name=data['name'])
  db.session.add(new_case)
  for x in data['location']:
      new_location = Location(city=x['city'], department=x['department'], comment=x['comment'], case_id=new_case.id)
      db.session.add(new_location)
  db.session.commit()
  #return make_response(jsonify({'message': 'case created'}), 201)
  return make_response(jsonify({'message': 'error creating case'}), 500)

# get all cases
@app.route('/get_all_cases', methods=['GET'])
def get_cases():
  try:
    cases = Case.query.all()
    return make_response(jsonify({'message': 'success'}), 200)
  except:
    return make_response(jsonify({'message': 'error getting cases'}), 500)

# get a case by id
@app.route('/get_case', methods=['GET'])
def get_case():
  data = request.json
  try:
    case = Case.query.filter_by(name=data['name']).first()
    if case:
      return make_response(jsonify({'message': 'success'}), 200)
    return make_response(jsonify({'message': 'case not found'}), 404)
  except:
    return make_response(jsonify({'message': 'error getting case'}), 500)

# update a case
@app.route('/update_case', methods=['PUT'])
def update_case(id):
  try:
    case = Case.query.filter_by(id=id).first()
    if case:
      data = request.get_json()
      case.name = data['name']
      case.location = data['location']
      db.session.commit()
      return make_response(jsonify({'message': 'case updated'}), 200)
    return make_response(jsonify({'message': 'case not found'}), 404)
  except:
    return make_response(jsonify({'message': 'error updating case'}), 500)

# delete a case
@app.route('/cases/<int:id>', methods=['DELETE'])
def delete_case(id):
  try:
    case = Case.query.filter_by(id=id).first()
    if case:
      db.session.delete(case)
      db.session.commit()
      return make_response(jsonify({'message': 'case deleted'}), 200)
    return make_response(jsonify({'message': 'case not found'}), 404)
  except:
    return make_response(jsonify({'message': 'error deleting case'}), 500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="4000", debug=True)