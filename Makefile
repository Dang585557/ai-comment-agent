.PHONY: install run backend dashboard test lint format docker-up docker-down clean

install:
	pip install -r requirements.txt

backend:
	uvicorn dashboard.backend.api:app --reload

dashboard:
	cd dashboard/frontend && npm install && npm run dev

run:
	make backend

test:
	pytest

lint:
	ruff check .

format:
	black .
	isort .

docker-up:
	docker compose up --build

docker-down:
	docker compose down

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
