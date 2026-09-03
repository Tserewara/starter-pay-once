# The payment that happened twice

This is the Ledgerloop charges service used in the exercise. It has a small HTTP API and an in-memory store so it starts quickly on a laptop.

## Run it

You need Docker with Compose. Start the API with:

```sh
make up
```

The health check is `curl http://localhost:8080/health`. Run the existing checks with `make test`, and stop the service with `make down`.

The local control endpoints reset the data with `make reset`. The TTL drill can advance the service clock by sending `X-Advance-Seconds` to `POST /_control/advance`.

## Try the traffic shape

`make load` sends forty concurrent attempts for one checkout and prints the number of stored charges. The service starts with the behavior that was handed to the team; the exercise is to change that behavior while keeping the given validation and response contract.

## API

`POST /v1/charges` accepts `amount` in cents, `currency` (`usd` or `eur`), and `customer`. `GET /charges` is a local inspection endpoint. No external payment provider is contacted.
