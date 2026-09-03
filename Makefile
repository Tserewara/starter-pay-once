.PHONY: up down test load reset

export COMPOSE_PROJECT_NAME=pay_once

up:
	docker compose up -d --build api

down:
	docker compose down --remove-orphans

test:
	docker compose run --rm --build test

load:
	docker compose run --rm --build test python3 tools/retry_storm.py

reset:
	curl -fsS -X POST http://localhost:8080/_control/reset
