from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from os import environ
from sqlalchemy import create_engine
import urllib
from sqlalchemy.orm import sessionmaker
from models import User, Registration, Vehicle, Insurer
import json


app = Flask(__name__)


engine = create_engine("mysql+pymysql://root:%s@localhost:3306/service_nsw" % urllib.parse.quote_plus('Princess@17'), echo=True)
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/registrations/<user_id>')
def get_registrations(user_id):
    query = session.query(User, Vehicle, Registration, Insurer)\
            .join(Registration, Vehicle.vin == Registration.vin)\
            .join(Insurer, Vehicle.vin == Insurer.vin)\
            .filter(User.user_id == user_id, User.user_id == Vehicle.user_id).all()


    resp = dict(registrations=[dict(plate_number=e.plate_number,
                                    registration=f.serializable,
                                    vehicle=e.serializable,
                                    insurer=g.serializable)
                                for c, e, f, g in query])

    a = json.dumps(resp)
    print(a)

    return "done"


if __name__ == "__main__":
    app.run()
