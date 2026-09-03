import json
import os
import urllib.error
import urllib.request
import unittest


BASE = os.environ.get("SERVICE_URL", "http://localhost:8080")


def request(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    headers = {"Content-Type": "application/json"} if data else {}
    req = urllib.request.Request(f"{BASE}{path}", data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=10) as response:
        return response.status, json.load(response)


class GivenApiTests(unittest.TestCase):
    def setUp(self):
        request("POST", "/_control/reset")

    def test_health(self):
        status, body = request("GET", "/health")
        self.assertEqual(status, 200)
        self.assertEqual(body["status"], "ok")

    def test_valid_charge_has_expected_response(self):
        status, body = request("POST", "/v1/charges", {"amount": 1200, "currency": "usd", "customer": "cus_test"})
        self.assertEqual(status, 201)
        self.assertEqual(body["status"], "succeeded")
        self.assertEqual(body["amount"], 1200)

    def test_invalid_amount_is_rejected(self):
        with self.assertRaises(urllib.error.HTTPError) as error:
            request("POST", "/v1/charges", {"amount": 0, "currency": "usd", "customer": "cus_test"})
        self.assertEqual(error.exception.code, 422)


if __name__ == "__main__":
    unittest.main()
