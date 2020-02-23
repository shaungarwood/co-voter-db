from flask import Flask
from flask import request
from flask import jsonify
from os import environ

import query

app = Flask(__name__)

if 'MONGODB_HOST' in environ:
    mongodb_host = environ['MONGODB_HOST']
else:
    mongodb_host = "localhost"

if 'MONGODB_PORT' in environ:
    mongodb_port = environ['MONGODB_PORT']
else:
    mongodb_port = "27017"

vr = query.VoterRecords(mongodb_host, mongodb_port)


@app.route('/search')
def search():
    if request.args and 'q' in request.args:
        search_string = request.args['q']
        res = vr.determine_query_type(search_string)
        resp = app.make_response(res)
        resp.mimetype = 'application/json'

        return jsonify(resp)
    else:
        return "No query data received", 200


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
