from typing import Dict

from flask import Flask
from flask import jsonify
from flask import request

from misc.sqlalchemy_example import *

app = Flask(__name__)
db = CrawlerDAO('postgresql://postgres:postgres@localhost:5432/tcrawler')

@app.route('/')
def hello():
    q = request.args.get('query','')
    return jsonify(
        [{
                    "id:": r['id'],
                    "bio": r['bio']
         }
            for r in db.listUsers(q)
        ])

if __name__ == '__main__':
    app.run()