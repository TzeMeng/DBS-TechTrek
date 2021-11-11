from datetime import datetime
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with, inputs
from flask_sqlalchemy import SQLAlchemy
from numpy import str0

app = Flask(__name__)
api = Api(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project_expenses.db'
db = SQLAlchemy(app)

#  Supporting code to add new expense to db
expense_post_args = reqparse.RequestParser()
expense_post_args.add_argument("Id", type=int, help="Expense ID is required", required=True)
expense_post_args.add_argument("Project_id", type=int, help="Project ID is required", required=True)
expense_post_args.add_argument("Category_id", type=int, help="Category ID is required", required=True)
expense_post_args.add_argument("Name", type=str, help="Expense name is required", required=True)
expense_post_args.add_argument("Description", type=str, help="Expense description is required", required=True)
expense_post_args.add_argument("Amount", type=int, help="Expense amount is required", required=True)
expense_post_args.add_argument("Created_at", type=str, help="When was this expense created?", required=False)
expense_post_args.add_argument("Created_by", type=str, help="Who created this expense?", required=True)
expense_post_args.add_argument("Updated_at", type=str, help="When was this expense updated?", required=False)
expense_post_args.add_argument("Updated_by", type=str, help="Who updated this expense?", required=True)

# Supporting code to update existing expense in db
expense_update_args = reqparse.RequestParser()
expense_update_args.add_argument("Id", type=int, help="Expense ID is required", required=True)
expense_update_args.add_argument("Name", type=str, help="Expense name is required", required=True)
expense_update_args.add_argument("Description", type=str, help="Expense description is required", required=True)
expense_update_args.add_argument("Amount", type=int, help="Expense amount is required", required=True)
expense_update_args.add_argument("Created_at", type=str, help="When was this expense created?", required=True)
expense_update_args.add_argument("Created_by", type=str, help="Who created this expense?", required=True)
expense_update_args.add_argument("Updated_at", type=str, help="When was this expense updated?", required=True)
expense_update_args.add_argument("Updated_by", type=str, help="Who updated this expense?", required=True)

# Supporting code to transform data and serialise it before being processed
resource_fields = {
    'Id': fields.Integer,
    'Project_id': fields.Integer,
    'Category_id': fields.Integer,
	'Name': fields.String,
    'Description': fields.String,
	'Amount': fields.Integer,
    'Created_at': fields.String,
    'Created_by': fields.String,
    'Updated_at': fields.String,
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
		if not result: abort(404, message="Expense doesn't exist")

		if args['Name']: result.Name = args['Name']
        # if args['Description']: result.Description = args['Description']
		if args['Amount']: result.Amount = args['Amount']
        # if args['Created_by']: result.Created_by = args['Created_by']
        # if args['Updated_by']: result.Updated_by = args['Updated_by']

		db.session.commit()

		return result

	def delete(self, expense_id):
        # To delete expense

		return '', 204

#  To add new expense to the db
class projectModel(db.Model): 
    Id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer, nullable=False)
    Name = db.Column(db.String(100), nullable=False)
    Description = db.Column(db.String(100), nullable=False)
    Budget = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'''project(ID = {Id}, User_id = {User_id}, Name = {Name}, \
            Description = {Description}, Budget = {Budget})''' 

# Main code to api calls (For project related stuffs)
# Code is able to: query, add, modify, delete
# get, post, patch, delete
class project(Resource):
    
	@marshal_with(resource_fields)
	def get(self, project_id):
        # To query existing project from table
		result = projectModel.query.filter_by(Id=project_id).first()
		if not result: abort(404, message="Could not find project with that ID")
		return result

	@marshal_with(resource_fields)
	def post(self, project_id):
        # To add new project
		args = project_post_args.parse_args()
		result = projectModel.query.filter_by(Id=project_id).first()
		if result: abort(409, message="Project ID taken")
        
		project = projectModel(Id=project_id, User_id=args['User_id'],\
                Name=args['Name'], Description=args['Description'], Budget=args['Budget'])
		db.session.add(project)
		db.session.commit()
		return project, 201

	@marshal_with(resource_fields)
	def patch(self, project_id):
        #  To modify project
		args = project_update_args.parse_args()
		result = projectModel.query.filter_by(Id=project_id).first()
		if not result:
			abort(404, message="project doesn't exist")

		if args['Name']: result.Name = args['Name']
		if args['Amount']: result.Amount = args['Amount']

		db.session.commit()

		return result

	def delete(self, project_id):
        # To delete project
		return '', 204

# To add route to flask for the api call
api.add_resource(project, "/projects/<int:user_id>") 
api.add_resource(expense, "/expense/<int:expense_id>") 
# api.add_resource(user, "/user/<int:user_id>") 

if __name__ == "__main__":
	app.run(debug=False)
