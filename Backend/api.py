from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)

#  Supporting code to add new expense to db
expense_put_args = reqparse.RequestParser()
expense_put_args.add_argument("Name", type=str, help="Expense name is required", required=True)
expense_put_args.add_argument("Description", type=str, help="Expense description is required", required=True)
expense_put_args.add_argument("Amount", type=int, help="Expense amount is required", required=True)
expense_put_args.add_argument("Created_by", type=str, help="Who created this expense?", required=True)
expense_put_args.add_argument("Updated_by", type=str, help="Who updated this expense?", required=True)

# Supporting code to update existing expense in db
expense_update_args = reqparse.RequestParser()
expense_update_args.add_argument("Name", type=str, help="Expense name is required", required=True)
expense_update_args.add_argument("Description", type=str, help="Expense description is required", required=True)
expense_update_args.add_argument("Amount", type=int, help="Expense amount is required", required=True)
expense_update_args.add_argument("Created_by", type=str, help="Who created this expense?", required=True)
expense_update_args.add_argument("Updated_by", type=str, help="Who updated this expense?", required=True)

# Supporting code to transform data and serialise it before being processed
    # 'Id': fields.Integer,
    # 'Project_id': fields.Integer,
    # 'Category_id': fields.Integer,
resource_fields = {
	'Name': fields.String,
    'Description': fields.String,
	'Amount': fields.Integer,
    'Created_by': fields.String,
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
    Created_by = db.Column(db.String(100), nullable=False)
    Updated_by = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'''expense(ID = {Id}, Project_id = {Project_id}, Category_id = {Category_id}, \
            Name = {Name}, Description = {Description}, Amount = {Amount}, \
            Created_by = {Created_by}, Updated_by = {Updated_by})'''

# Main code to api calls (For expense related stuffs)
# Code is able to: query, add, modify, delete
class expense(Resource):
	@marshal_with(resource_fields)
	def get(self, expense_id):
        # To query existing expense from table
		result = expenseModel.query.filter_by(Id=expense_id).first()
		if not result: abort(404, message="Could not find expense with that ID")
		return result

	@marshal_with(resource_fields)
	def put(self, expense_id):
        # To add new expense
		args = expense_put_args.parse_args()
		result = expenseModel.query.filter_by(Id=expense_id).first()
		if result: abort(409, message="Expense ID taken")

		expense = expenseModel(Id=expense_id, Name=args['Name'], Amount=args['Amount'])
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
		if args['Amount']: result.Amount = args['Amount']

		db.session.commit()

		return result

	def delete(self, expense_id):
        # To delete expense
		abort_if_expense_id_doesnt_exist(expense_id)
		del expenses[expense_id]
		return '', 204

# To add route to flask for the api call
# api.add_resource(projects, "/projects/<int:project_id>") 
api.add_resource(expense, "/Id/<int:expense_id>") 

if __name__ == "__main__":
	app.run(debug=False)
