import unittest
from fastapi.testclient import TestClient
from api_service import app

client = TestClient(app)

class APITest(unittest.TestCase):

    def test_home(self):

        response = client.get("/")

        self.assertEqual(response.status_code,200)

    def test_prediction(self):

        response = client.post(
            "/predict",
            json={"text":"This movie is amazing"}
        )

        self.assertEqual(response.status_code,200)

        data = response.json()

        self.assertIn("sentiment",data)

if __name__ == "__main__":
    unittest.main()