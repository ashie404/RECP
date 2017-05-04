#!flask/bin/python

# This above is the directory to the virtual environment I'm running this in ^

# RECS | REST Chat Server | Main file
# Server runner
# Built off of Flask and Python 3 by Joyesh.

# Import statements
from flask import Flask, jsonify, request

# RECS Flask app
app = Flask(__name__)

# Variables

# Run in debug mode (Allows people to execute python code on your computer! Do not use this in production)
debug = True

# HTTP status codes
HTTP_STATUS_CODES = {
        '200' : 'OK',
        '201' : 'Created',
        '202' : 'Accepted',
        '203' : 'Non-Authoritative Information',
        '204' : 'No Content',
        '205' : 'Reset Content',
        '206' : 'Partial Content',
        '300' : 'Multiple Choices',
        '301' : 'Moved Permanently',
        '302' : 'Found',
        '303' : 'See Other',
        '304' : 'Not Modified',
        '305' : 'Use Proxy',
        '307' : 'Temporary Redirect',
        '400' : 'Bad Request',
        '401' : 'Unauthorized',
        '402' : 'Payment Required',
        '403' : 'Forbidden',
        '404' : 'Not Found',
        '405' : 'Method Not Allowed',
        '406' : 'Not Acceptable',
        '407' : 'Proxy Authentication Required',
        '408' : 'Request Timeout',
        '409' : 'Conflict',
        '410' : 'Gone',
        '411' : 'Length Required',
        '412' : 'Precondition Failed',
        '413' : 'Request Entity Too Large',
        '414' : 'Request-URI Too Long',
        '415' : 'Unsupported Media Type',
        '416' : 'Requested Range Not Satisfiable',
        '417' : 'Expectation Failed',
        '500' : 'Internal Server Error',
        '501' : 'Not Implemented',
        '502' : 'Bad Gateway',
        '503' : 'Service Unavailable',
        '504' : 'Gateway Timeout',
        '505' : 'HTTP Version Not Supported'
};

messages = [
    {
        "id": 0,
        "authorid": 0,
        "content": "Successfully started RECS!",
        "edited": False
    }
];

# Main app

# Send a HTTP error in JSON format

def httpcode(error):
    return jsonify({str(error): HTTP_STATUS_CODES[str(error)]})

# Get all messages
@app.route('/recs/api/v1.0/message', methods=['GET'])
def get_messages():
    # Return all messages. This will probably be changed later on.
    return jsonify({'messages': messages})

# Add message
@app.route('/recs/api/v1.0/message', methods=['POST'])
def send_message():
    # Return 400 if they don't have required variables.
    if not request.json or not 'authorid' in request.json or not 'content' in request.json:
        return httpcode(400)

    # Create a custom message object to prevent them adding variables themselves.
    message = {
        'id': messages[-1]['id'] + 1,
        'authorid': request.json['authorid'],
        'content': request.json['content'],
        'edited': False
    }
    # Add the message.
    messages.append(message)

    # Return HTTP 201
    return httpcode(200)

# Delete message
@app.route('/recs/api/v1.0/message/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    # Get message.
    message = [message for message in messages if message['id'] == message_id]
    # If the message doesn't exist, return 404 not found.
    if len(message) == 0:
        return httpcode(404)

    # Remove message
    messages.remove(message[0])
    # Return HTTP 201
    return httpcode(200)

# Edit message
@app.route('/recs/api/v1.0/message/<int:message_id>', methods=['PUT'])
def edit_message(message_id):
    # Get message
    message = [message for message in messages if message['id'] == message_id]
    # If the message doesn't exist, return 404 not found
    if len(message) == 0:
        return httpcode(404)
    # If they didn't include content
    if not 'content' in request.json:
        return httpcode(400)

    # Create a new message object based off of the old one.

    newmessage = {
        'id': message[0]['id'],
        'authorid': message[0]['authorid'],
        'content': request.json['content'],
        'edited': True
    }


    # Edit message
    i = 0
    for messagea in messages:
        if messagea['id'] == message_id:
            messages[i] = newmessage
        i = i+1

    # Success!
    return httpcode(200)

# Run app
if __name__ == '__main__':
    # If we're in debug mode or not
    if debug:
        app.run(debug=True)
    else:
        app.run()
