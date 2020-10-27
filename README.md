**Vehicle Registration GET api**

This application requires:
- Python 3.8.6
- sqlite3

Install the requirements using:
```
pip install -r requirements.txt
```

To populate the database with some sample values:
```
python populate_db.py
```

To run the application (this will start the flask server - default port is 5000):

```
python run_server.py
```

Hit the endpoint:

```
curl localhost:5000/registrations/50
```

You should see the response:

```
{
   "registrations":[
      {
         "insurer":{
            "code":13,
            "name":"GIO"
         },
         "plate_number":"CXD89G",
         "registration":{
            "expired":true,
            "expiry_date":"2020-10-27T17:35:46.835Z"
         },
         "vehicle":{
            "colour":"Blue",
            "gross_mass":null,
            "make":"Mercedes",
            "model":"X4 M40i",
            "tare_weight":1700,
            "type":"Sedan",
            "vin":"87676676762"
         }
      },
      {
         "insurer":{
            "code":27,
            "name":"NRMA"
         },
         "plate_number":"EMD82G",
         "registration":{
            "expired":true,
            "expiry_date":"2020-10-27T17:35:46.835Z"
         },
         "vehicle":{
            "colour":"Navy Blue",
            "gross_mass":null,
            "make":"Jaguar",
            "model":"XJ",
            "tare_weight":1620,
            "type":"SUV",
            "vin":"65465466541"
         }
      }
   ]
}

```

To run the tests:

```
python -m unittest tests
```

To format the code, [Black is used](https://github.com/psf/black) which follows PEP8 standards:

```
black .
```

Some assumptions and notes:

- In this application I am using serializable for the models to return the schema as per the specs for the GET api
. However in practice, application schemas will differ for different endpoints. 
- I am using the same sqlite db file for development and testing. But in actual project, there should be different database for testing,
which should ideally be dropped after the testing has completed. 
For the same purpose, different configurations can be used for testing/development/production.
- The existing tests check the response of the API. However, more tests can be added to check the validity of data, inputs and outputs etc.
- This application can be used for postgres or mysql as well. For this SQLALCHEMY_DATABASE_URI should be changed.