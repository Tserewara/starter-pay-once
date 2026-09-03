import threading

_lock = threading.Lock()
_charges = []
_clock_offset = 0.0


def now():
    import time

    return time.time() + _clock_offset


def advance(seconds):
    global _clock_offset
    _clock_offset += seconds


def reset():
    global _clock_offset
    with _lock:
        _charges.clear()
        _clock_offset = 0.0


def create_charge(body):
    with _lock:
        charge = {
            "charge_id": f"ch_{len(_charges) + 1:04d}",
            "amount": body["amount"],
            "currency": body["currency"],
            "customer": body["customer"],
            "created_at": now(),
        }
        _charges.append(charge)
        return dict(charge)


def all_charges():
    with _lock:
        return [dict(charge) for charge in _charges]
