import json
import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor

BASE = os.environ.get("SERVICE_URL", "http://localhost:8080")
BODY = json.dumps({"amount": 18600, "currency": "usd", "customer": "cus_017"}).encode()

urllib.request.urlopen(urllib.request.Request(f"{BASE}/_control/reset", method="POST")).close()


def send(_):
    request = urllib.request.Request(
        f"{BASE}/v1/charges",
        data=BODY,
        headers={"Content-Type": "application/json", "Idempotency-Key": "storm-017"},
    )
    with urllib.request.urlopen(request, timeout=10) as response:
        return response.status


with ThreadPoolExecutor(max_workers=20) as pool:
    statuses = list(pool.map(send, range(40)))
with urllib.request.urlopen(f"{BASE}/charges") as response:
    charges = json.load(response)["charges"]
print(f"requests={len(statuses)} statuses={sorted(set(statuses))} charges={len(charges)} duplicate_charges={max(0, len(charges) - 1)}")
