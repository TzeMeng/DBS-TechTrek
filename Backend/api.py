from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import create_access_token, JWTManager

### Firebase
import os
import firebase
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app


cred = credentials.Certificate('key.json')

firebase_admin.initialize_app(cred)

db = firestore.client()
todo_ref = db.collection('users')

app = Flask(__name__)
api = Api(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project_expenses.db'
db = SQLAlchemy(app)

app.config["JWT_SECRET_KEY"] = "verysecretkey"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)

#  Supporting code to add new expense to db
expense_post_args = reqparse.RequestParser()
expense_post_args.add_argument("Name", type=str, help="Expense name is required", required=True)
expense_post_args.add_argument("Description", type=str, help="Expense description is required", required=True)
expense_post_args.add_argument("Amount", type=int, help="Expense amount is required", required=True)
expense_post_args.add_argument("Created_at", type=datetime, help="When was this expense created?", required=True)
expense_post_args.add_argument("Created_by", type=str, help="Who created this expense?", required=True)
expense_post_args.add_argument("Updated_at", type=datetime, help="When was this expense updated?", required=True)
expense_post_args.add_argument("Updated_by", type=str, help="Who updated this expense?", required=True)

# Supporting code to update existing expense in db
expense_update_args = reqparse.RequestParser()
expense_update_args.add_argument("Name", type=str, help="Expense name is required", required=True)
expense_update_args.add_argument("Description", type=str, help="Expense description is required", required=True)
expense_update_args.add_argument("Amount", type=int, help="Expense amount is required", required=True)
expense_update_args.add_argument("Created_at", type=datetime, help="When was this expense created?", required=True)
expense_update_args.add_argument("Created_by", type=str, help="Who created this expense?", required=True)
expense_update_args.add_argument("Updated_at", type=datetime, help="When was this expense updated?", required=True)
expense_update_args.add_argument("Updated_by", type=str, help="Who updated this expense?", required=True)

# Supporting code to transform data and serialise it before being processed
resource_fields = {
    'Id': fields.Integer,
    'Project_id': fields.Integer,
    'Category_id': fields.Integer,
	'Name': fields.String,
    'Description': fields.String,
	'Amount': fields.Integer,
    'Created_at': fields.DateTime,
    'Created_by': fields.String,
    'Updated_at': fields.DateTime,
    'Updated_by': fields.String,
}

#  To add new expense to the db
class expenseModel(db.Model): 
    Id = db.Column(db.Integer, primary_key=True)
    Project_id = db.Column(db.Integer, nullable=False)
    Category_id= db.Column(db.Integer, nullable=False)
    Name = db.Column(db.String(100), nullable=False)
    Description = db.Column(db.String(100), nullable=False)
    Amount = db.Column(db.Integer, nullable=False)
    Created_at = db.Column(db.DateTime, nullable=False)
    Created_by = db.Column(db.String(100), nullable=False)
    Updated_at = db.Column(db.DateTime, nullable=False)
    Updated_by = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'''expense(ID = {Id}, Project_id = {Project_id}, Category_id = {Category_id}, \
            Name = {Name}, Description = {Description}, Amount = {Amount}, \
            Created_at = {Created_at}, Created_by = {Created_by}, \
            Updated_at = {Updated_at}, Updated_by = {Updated_by})'''

# Main code to api calls (For expense related stuffs)
# Code is able to: query, add, modify, delete
# get, post, patch, delete
class expense(Resource):
    
	@marshal_with(resource_fields)
	def get(self, expense_id):
        # To query existing expense from table
		result = expenseModel.query.filter_by(Id=expense_id).first()
		if not result: abort(404, message="Could not find expense with that ID")
		return result

	@marshal_with(resource_fields)
	def post(self, expense_id):
        # To add new expense
		args = expense_post_args.parse_args()
		result = expenseModel.query.filter_by(Id=expense_id).first()
		if result: abort(409, message="Expense ID taken")
        
		expense = expenseModel(Id=expense_id, Project_id=args['Project_id'], Category_id=args['Category_id'],\
                Name=args['Name'], Description=args['Description'], Amount=args['Amount'],\
                Created_at=args['Created_at'], Created_by=args['Created_by'],\
                Updated_at=args['Updated_at'], Updated_by=args['Updated_by'])
		db.session.add(expense)
		db.session.commit()
		return expense, 201

	@marshal_with(resource_fields)
	def patch(self, expense_id):
        #  To modify expense
		args = expense_update_args.parse_args()
		result = expenseModel.query.filter_by(Id=expense_id).first()
		if not result:
			abort(404, message="Expense doesn't exist")

		if args['Name']: result.Name = args['Name']
        # if args['Description']: result.Description = args['Description']
		if args['Amount']: result.Amount = args['Amount']
        # if args['Created_by']: result.Created_by = args['Created_by']
        # if args['Updated_by']: result.Updated_by = args['Updated_by']

		db.session.commit()

		return result

	def delete(self, expense_id):
        # To delete expense
		abort_if_expense_id_doesnt_exist(expense_id)
		del expenses[expense_id]
		return '', 204

# To add route to flask for the api call
# api.add_resource(projects, "/projects/<int:user_id>") 
api.add_resource(expense, "/expense/<int:expense_id>") 

# Authentication code
@app.route("/login", methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    try:
        # Check if ID was passed to URL query
        todo_id = request.args.get('username')    
        if todo_id:
            todo = todo_ref.document(todo_id).get()
            data = jsonify(todo.to_dict()), 200
        else:
            all_todos = [doc.to_dict() for doc in todo_ref.stream()]
            data =  jsonify(all_todos), 200
    
        for user in data:
            if user["username"] == username and user["password"] == password:
                return jsonify(access_token=access_token, user["id"])
            
        return jsonify({"msg": "Bad username or password"}), 401


    except Exception as e:
        return jsonify({"msg": "Bad username or password"}), 401



if __name__ == "__main__":
	app.run(debug=False)
