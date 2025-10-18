.PHONY: help install backend-install frontend-install run backend frontend docker-up docker-down clean test

help:
	@echo "TrippiTroppi - Makefile commands"
	@echo ""
	@echo "Installation:"
	@echo "  make install           - Install all dependencies (backend + frontend)"
	@echo "  make backend-install   - Install backend dependencies"
	@echo "  make frontend-install  - Install frontend dependencies"
	@echo ""
	@echo "Running:"
	@echo "  make backend           - Run backend server"
	@echo "  make frontend          - Run Flutter app"
	@echo "  make docker-up         - Start Docker containers"
	@echo "  make docker-down       - Stop Docker containers"
	@echo ""
	@echo "Database:"
	@echo "  make db-migrate        - Create new migration"
	@echo "  make db-upgrade        - Apply migrations"
	@echo "  make db-downgrade      - Rollback migration"
	@echo ""
	@echo "Other:"
	@echo "  make clean             - Clean temporary files"
	@echo "  make test              - Run tests"
	@echo "  make lint              - Run linters"

# Installation
install: backend-install frontend-install

backend-install:
	cd backend && python -m venv venv && \
	. venv/bin/activate && \
	pip install -r requirements.txt

frontend-install:
	cd frontend && flutter pub get

# Running
backend:
	cd backend && . venv/bin/activate && \
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

frontend:
	cd frontend && flutter run

# Docker
docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f

docker-rebuild:
	docker-compose down && docker-compose build && docker-compose up -d

# Database
db-migrate:
	cd backend && . venv/bin/activate && \
	alembic revision --autogenerate -m "$(message)"

db-upgrade:
	cd backend && . venv/bin/activate && \
	alembic upgrade head

db-downgrade:
	cd backend && . venv/bin/activate && \
	alembic downgrade -1

db-reset:
	cd backend && . venv/bin/activate && \
	alembic downgrade base && alembic upgrade head

# Testing
test:
	cd backend && . venv/bin/activate && pytest tests/
	cd frontend && flutter test

# Linting
lint:
	cd backend && . venv/bin/activate && \
	black app/ && isort app/ && flake8 app/
	cd frontend && flutter analyze

# Cleaning
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	cd frontend && flutter clean

