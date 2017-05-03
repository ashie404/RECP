#!flask/bin/python

# RECS | REST Chat Server | Main file
# Server runner
# Built off of Flask and Python 3 by Joyesh.

# Import statements
from flask import Flask, jsonify, request

# RECS Flask app
app = Flask(__name__)

messages = [
    {
        'id': 1,
        'authorid': 1,
        'content': u'Hello world!'
    },
]

# Get all messages
@app.route('/recs/api/v1.0/message', methods=['GET'])
def get_messages():
    return jsonify({'messages': messages})

# Add message
@app.route('/recs/api/v1.0/message', methods=['POST'])
def send_message():
    if not request.json or not 'authorid' in request.json or not 'content' in request.json:
        abort(400)

    message = {
        'id': messages[-1]['id'] + 1,
        'authorid': request.json['authorid'],
        'content': request.json['content']
    }
    messages.append(message)
    return jsonify({'message': message}), 201

if __name__ == '__main__':
    app.run(debug=True)
