import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import storage


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return

    def send_json(self, status, payload):
        encoded = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def read_json(self):
        length = int(self.headers.get("Content-Length", "0"))
        return json.loads(self.rfile.read(length))

    def do_GET(self):
        if self.path == "/health":
            self.send_json(200, {"status": "ok"})
        elif self.path == "/charges":
            self.send_json(200, {"charges": storage.all_charges()})
        else:
            self.send_json(404, {"error": "not_found"})

    def do_POST(self):
        if self.path == "/v1/charges":
            try:
                body = self.read_json()
                if not isinstance(body.get("amount"), int) or body["amount"] <= 0:
                    raise ValueError("amount must be a positive integer")
                if body.get("currency") not in {"usd", "eur"}:
                    raise ValueError("currency must be usd or eur")
                if not body.get("customer"):
                    raise ValueError("customer is required")
            except (ValueError, json.JSONDecodeError, TypeError) as exc:
                self.send_json(422, {"error": str(exc)})
                return
            charge = storage.create_charge(body)
            self.send_json(201, {"charge_id": charge["charge_id"], "status": "succeeded", "amount": charge["amount"], "currency": charge["currency"]})
        elif self.path == "/_control/reset":
            storage.reset()
            self.send_json(200, {"status": "reset"})
        elif self.path == "/_control/advance":
            try:
                seconds = float(self.headers.get("X-Advance-Seconds", "0"))
            except ValueError:
                seconds = 0
            storage.advance(seconds)
            self.send_json(200, {"advanced_seconds": seconds})
        else:
            self.send_json(404, {"error": "not_found"})


if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
