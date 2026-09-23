# The payment that happened twice

This is Ledgerloop's charge service, cut down to what the exercise needs: a small HTTP API and an in-memory store, so it starts in a couple of seconds on a laptop.

## Run it

You need Docker with Compose.

```sh
make up
```

`curl http://localhost:8080/health` tells you it's up. `make test` runs the existing checks and `make down` stops everything.

`make reset` wipes the stored charges. For the expiry drill, `POST /_control/advance` moves the service clock forward by the number of seconds in its `X-Advance-Seconds` header.

## Replay Friday

`make load` sends forty concurrent attempts at one checkout, all with the same `Idempotency-Key`, and prints one line:

```
requests=40 statuses=[...] charges=N duplicate_charges=N
```

The service still behaves the way it did on Friday. Your job is to change that while keeping the validation and the response contract it already has.

## API

`POST /v1/charges` takes `amount` in cents, `currency` (`usd` or `eur`) and `customer`. `GET /charges` lists what's stored, for inspection. Nothing talks to a real payment provider.
