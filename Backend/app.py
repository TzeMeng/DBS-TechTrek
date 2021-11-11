# Required Imports
import os
import firebase
import firebase_admin
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
# Initialize Flask App


app = Flask(__name__)
# Initialize Firestore DB
cred = credentials.Certificate('key.json')

firebase_admin.initialize_app(cred)

db = firestore.client()
todo_ref = db.collection('users')

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_user():
    """
        read() : Fetches documents from Firestore collection as JSON
        todo : Return document that matches query ID
        all_todos : Return all documents
    """
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
            if


    except Exception as e:
        return f"An Error Occured: {e}"
    

if __name__ == "__main__":
    app.run()