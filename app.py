import json

from flask import Flask
from flask import request

app = Flask(__name__)

import query

@app.route('/search')
def search():
    if request.args and 'q' in request.args:
        search_string = request.args['q']
        res = query.determine_query_type(search_string)
        return json.dumps(res)
    else:
        return "No query data received", 200

if __name__ == '__main__':
    app.run()
