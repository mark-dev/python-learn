from typing import Dict

from flask import Flask
from flask import jsonify

from misc.sqlalchemy_example import *

app = Flask(__name__)
db = DataBaseWrapper()

class SelfDrivingCar:
    id = None
    name = None

    def __init__(self,id,name) -> None:
        super().__init__()
        self.id = id
        self.name = name

    def serialize(self) -> Dict:
        return {'id': self.id,
                'name': self.name}

@app.route('/')
def hello():
    # d = {"k":3,"v": 44}
    # d1 = [SelfDrivingCar(3,"abc")]
    # return jsonify([d.serialize() for d in d1])
    return jsonify([{"id:": r['id'], "bio": r['bio']} for r in db.listUsers()])

if __name__ == '__main__':
    app.run()