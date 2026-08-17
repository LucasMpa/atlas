.PHONY: run tests migrate

run:
	uv run uvicorn atlas.main:app --reload --app-dir src

tests:
	uv run python -m unittest discover -s tests -v

migrate:
	set -a; . ./.env; set +a; uv run alembic upgrade head
