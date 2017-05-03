#!flask/bin/python

# RECS | REST Chat Server | Main file
# Server runner
# Built off of Flask and Python 3 by Joyesh.

# Import statements
from flask import Flask, jsonify, request

# RECS Flask app
app = Flask(__name__)

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
        'id': 1,
        'authorid': 1,
        'content': u'Hello world!'
    },
]

def abort(error):
    return jsonify({str(error): HTTP_STATUS_CODES[str(error)]})

# Get all messages
@app.route('/recs/api/v1.0/message', methods=['GET'])
def get_messages():
    return jsonify({'messages': messages})

# Add message
@app.route('/recs/api/v1.0/message', methods=['POST'])
def send_message():
    if not request.json or not 'authorid' in request.json or not 'content' in request.json:
        return abort(400)

    message = {
        'id': messages[-1]['id'] + 1,
        'authorid': request.json['authorid'],
        'content': request.json['content']
    }
    messages.append(message)
    return jsonify({'message': message}), 201

@app.route('/recs/api/v1.0/message/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    message = [message for message in messages if message['id'] == message_id]
    if len(message) == 0:
        abort(404)
    messages.remove(message[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
