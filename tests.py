import unittest
from app import app
import json


class VehicleRegistrationTest(unittest.TestCase):
    """
    Basic tests to check the status and response of API's
    """

    client = app.test_client()

    def test_connection_successful(self):
        response = self.client.get("/")
        self.assertTrue(response.status_code == 200)

    def test_registration_api_with_response(self):
        self.maxDiff = None
        response_1 = self.client.get("/registrations/50")
        self.assertTrue(response_1.status_code == 200)
        actual_response = json.loads(response_1.get_data(as_text=True))
        self.assertEqual(len(actual_response["registrations"]), 2)
        self.assertEqual(
            actual_response["registrations"][0]["vehicle"]["vin"], "87676676762"
        )
        self.assertEqual(actual_response["registrations"][0]["plate_number"], "CXD89G")
        self.assertEqual(actual_response["registrations"][1]["plate_number"], "EMD82G")
        self.assertEqual(actual_response["registrations"][0]["insurer"]["code"], 13)
        self.assertEqual(actual_response["registrations"][1]["insurer"]["code"], 27)

        response_1 = self.client.get("/registrations/40")
        self.assertTrue(response_1.status_code == 200)
        actual_response = json.loads(response_1.get_data(as_text=True))
        self.assertEqual(len(actual_response["registrations"]), 2)
        self.assertEqual(
            actual_response["registrations"][0]["vehicle"]["vin"], "12389347324"
        )
        self.assertEqual(actual_response["registrations"][0]["plate_number"], "CXD82F")
        self.assertEqual(actual_response["registrations"][1]["plate_number"], "CXD82G")
        self.assertEqual(actual_response["registrations"][0]["insurer"]["code"], 32)
        self.assertEqual(actual_response["registrations"][1]["insurer"]["code"], 17)

    def test_registration_api_with_empty_response(self):
        self.maxDiff = None
        response_1 = self.client.get("/registrations/60")
        self.assertTrue(response_1.status_code == 200)
        actual_response = json.loads(response_1.get_data(as_text=True))
        self.assertEqual(actual_response, {"registrations": []})

    def test_registration_api_non_existent_route(self):
        response_1 = self.client.get("/vehicle/registrations")
        self.assertTrue(response_1.status_code == 404)


if __name__ == "__main__":
    unittest.main()
