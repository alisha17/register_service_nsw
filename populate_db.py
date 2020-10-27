from app import db
from app.models import User, Registration, Vehicle, Insurer
import datetime


def populate_db(db):
    """
    Populate the database with sample data
    """
    print("POPULATING DB...")
    db.create_all()

    db.session.add_all(
        [User(user_id=40, user_name="Alisha"), User(user_id=50, user_name="Akshat")]
    )

    db.session.commit()

    print("added users")

    db.session.add_all(
        [
            Vehicle(
                vin="12389347324",
                user_id=40,
                type="Wagon",
                make="BMW",
                model="X4 M40i",
                colour="Silver",
                tare_weight=1700,
                gross_mass=None,
                plate_number="CXD82F",
            ),
            Vehicle(
                vin="54646546313",
                user_id=40,
                type="Hatch",
                make="Toyota",
                model="X4 M40i",
                colour="Blue",
                tare_weight=1432,
                gross_mass=1500,
                plate_number="CXD82G",
            ),
            Vehicle(
                vin="87676676762",
                user_id=50,
                type="Sedan",
                make="Mercedes",
                model="X4 M40i",
                colour="Blue",
                tare_weight=1700,
                gross_mass=None,
                plate_number="CXD89G",
            ),
            Vehicle(
                vin="65465466541",
                user_id=50,
                type="SUV",
                make="Jaguar",
                model="XJ",
                colour="Navy Blue",
                tare_weight=1620,
                gross_mass=None,
                plate_number="EMD82G",
            ),
        ]
    )

    db.session.commit()

    print("added vehicles")

    db.session.add_all(
        [
            Registration(
                vin="12389347324",
                expired=True,
                expiry_date=datetime.datetime.now()
            ),
            Registration(
                vin="54646546313",
                expired=False,
                expiry_date=datetime.datetime.now()
            ),
            Registration(
                vin="87676676762",
                expired=True,
                expiry_date=datetime.datetime.now()
            ),
            Registration(
                vin="65465466541",
                expired=True,
                expiry_date=datetime.datetime.now()
            ),
            Insurer(
                vin="12389347324",
                name="Allianz",
                code=32),
            Insurer(
                vin="54646546313",
                name="AAMI",
                code=17),
            Insurer(
                vin="87676676762",
                name="GIO",
                code=13),
            Insurer(
                vin="65465466541",
                name="NRMA",
                code=27),
        ]
    )

    db.session.commit()

    print("DB populated!")


populate_db(db)
