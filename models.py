import sqlalchemy
from flask import Flask
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from os import environ
from sqlalchemy import create_engine
import urllib
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

# db_uri = environ.get('DB_URI')
engine = create_engine("mysql+pymysql://root:%s@localhost:3306/service_nsw" % urllib.parse.quote_plus('Princess@17'), echo=True)
# engine = create_engine('postgres://user:%s@host/database' % urlquote('badpass'))


class Vehicle(Base):
    __tablename__ = "vehicle"

    vin = Column(String(20), primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    type = Column(String(20))
    make = Column(String(20))
    model = Column(String(20))
    colour = Column(String(20))
    tare_weight = Column(Integer)
    gross_mass = Column(Integer)
    plate_number = Column(String(10), nullable=False)

    @property
    def serializable(self):
        return {'vin': self.vin,
                'type': self.type,
                'make': self.make,
                'model': self.model,
                'colour': self.colour,
                'tare_weight': self.tare_weight,
                'gross_mass': self.gross_mass}


class Registration(Base):
    __tablename__ = "registration"

    id = Column(Integer, primary_key=True)
    vin = Column(
        String(20),
        ForeignKey('vehicle.vin'),
        nullable=False
    )
    expired = Column(Boolean)
    expiry_date = Column(DateTime)

    @property
    def serializable(self):
        return {'expired': self.expired,
                'expiry_date': str(self.expiry_date.isoformat(timespec='milliseconds')+ 'Z')}



class Insurer(Base):
    __tablename__ = "insurer"

    id = Column(Integer, primary_key=True)
    vin = Column(String(20), ForeignKey('vehicle.vin'), nullable=False)
    name = Column(String(20))
    code = Column(Integer)

    @property
    def serializable(self):
        return {
                'name': self.name,
                'code': self.code
                }


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, nullable=False)
    user_name = Column(String(50), nullable=False)




Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()
#
# session.add_all([
#                 Vehicle(vin="12389347324", user_id=1, type="Wagon",make="BMW",model="X4 M40i",colour="Silver",tare_weight=1700,gross_mass=None),
#                 Vehicle(vin="54646546313", user_id=1, type="Hatch",make="Toyota",model="X4 M40i",colour="Blue",tare_weight=1432,gross_mass=1500),
#                 Vehicle(vin="87676676762", user_id=2, type="Sedan",make="Mercedes",model="X4 M40i",colour="Blue",tare_weight=1700,gross_mass=None),
#                 Vehicle(vin="65465466541", user_id=2, type="SUV",make="Jaguar",model="XJ",colour="Navy Blue",tare_weight=1620,gross_mass=None),
#                 Registration(vin="12389347324", expired=True,expiry_date="2020-03-01 23:15:30"),
#                 Registration(vin="54646546313", expired=False,expiry_date="2020-12-08 23:15:30"),
#                 Registration(vin="87676676762", expired=True,expiry_date="2020-03-01 23:15:30"),
#                 Registration(vin="65465466541", expired=True,expiry_date="2020-03-01 23:15:30"),
#                 Insurer(vin="12389347324", name="Allianz", code=32),
#                 Insurer(vin="54646546313", name="AAMI", code=17),
#                 Insurer(vin="87676676762", name="GIO", code=13),
#                 Insurer(vin="65465466541", name="NRMA", code=27)])
#
#
#
# session.commit()