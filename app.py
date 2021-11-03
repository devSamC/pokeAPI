from flask import Flask, jsonify, request
from flask_cors import CORS 
from werkzeug import exceptions


app = Flask(__name__)
CORS(app)

@app.route('/') # @<var-you-set-to-Flask(__name__)>
def home(): # this will run when a GET request to '/' is made
    return 'Hello from Flask!' # this plain-text will be sent in the response

@app.route('/cats', methods=['GET', 'POST'])
def cats_handler():
    if request.method == 'GET':
        return jsonify(['Ziggy', 'Zelda']), 200
    if request.method == 'POST':
       data = request.json
       return f"You created a cat! The cat is allowed {data['name']}", 200

@app.route('/cats/<int:cat_id>')
def cat_handler(cat_id):
    pass 

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({'message': f"Oops... {err}"}), 404

def handle_500(err):
    return jsonify({'message': f"Sorry we have a {err} Hopefully we will get it fixed soon"}), 500


if __name__ == '__main__':
    app.run(debug=True)

