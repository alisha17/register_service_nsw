from models import User, Registration, Vehicle, Insurer

Session = sessionmaker(bind=engine)
session = Session()


session.add_all([
    User(user_name="Alisha"),
    User(user_name="Akshat")
])

session.add_all([
                Vehicle(vin="12389347324", user_id=1, type="Wagon",make="BMW",model="X4 M40i",colour="Silver",tare_weight=1700,gross_mass=None),
                Vehicle(vin="54646546313", user_id=1, type="Hatch",make="Toyota",model="X4 M40i",colour="Blue",tare_weight=1432,gross_mass=1500),
                Vehicle(vin="87676676762", user_id=2, type="Sedan",make="Mercedes",model="X4 M40i",colour="Blue",tare_weight=1700,gross_mass=None),
                Vehicle(vin="65465466541", user_id=2, type="SUV",make="Jaguar",model="XJ",colour="Navy Blue",tare_weight=1620,gross_mass=None)])


session.add_all([
    Registration(vin="12389347324", expired=True, expiry_date="2020-03-01 23:15:30"),
    Registration(vin="54646546313", expired=False, expiry_date="2020-12-08 23:15:30"),
    Registration(vin="87676676762", expired=True, expiry_date="2020-03-01 23:15:30"),
    Registration(vin="65465466541", expired=True, expiry_date="2020-03-01 23:15:30"),
    Insurer(vin="12389347324", name="Allianz", code=32),
    Insurer(vin="54646546313", name="AAMI", code=17),
    Insurer(vin="87676676762", name="GIO", code=13),
    Insurer(vin="65465466541", name="NRMA", code=27)])
])




session.commit()