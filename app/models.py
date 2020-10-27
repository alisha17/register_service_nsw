from app import db


class Vehicle(db.Model):
    """
    Mapping for table 'vehicle'
    """

    __tablename__ = "vehicle"

    vin = db.Column(db.String(20), primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    type = db.Column(db.String(20))
    make = db.Column(db.String(20))
    model = db.Column(db.String(20))
    colour = db.Column(db.String(20))
    tare_weight = db.Column(db.Integer)
    gross_mass = db.Column(db.Integer)
    plate_number = db.Column(db.String(10), unique=True, nullable=False)

    @property
    def serializable(self):
        return {
            "vin": self.vin,
            "type": self.type,
            "make": self.make,
            "model": self.model,
            "colour": self.colour,
            "tare_weight": self.tare_weight,
            "gross_mass": self.gross_mass,
        }


class Registration(db.Model):
    """
    Mapping for table 'registration'
    """

    __tablename__ = "registration"

    id = db.Column(db.Integer, primary_key=True)
    vin = db.Column(db.String(20), db.ForeignKey("vehicle.vin"), nullable=False)
    expired = db.Column(db.Boolean)
    expiry_date = db.Column(db.DateTime)

    @property
    def serializable(self):
        return {
            "expired": self.expired,
            "expiry_date": str(
                self.expiry_date.isoformat(timespec="milliseconds") + "Z"
            ),
        }


class Insurer(db.Model):
    """
    Mapping for table 'insurer'
    """

    __tablename__ = "insurer"

    id = db.Column(db.Integer, primary_key=True)
    vin = db.Column(db.String(20), db.ForeignKey("vehicle.vin"), nullable=False)
    name = db.Column(db.String(20))
    code = db.Column(db.Integer)

    @property
    def serializable(self):
        return {"name": self.name, "code": self.code}


class User(db.Model):
    """
    Mapping for table 'user'
    """

    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
