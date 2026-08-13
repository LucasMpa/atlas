.PHONY: run tests

run:
	uv run uvicorn atlas.main:app --reload --app-dir src

tests:
	uv run python -m unittest discover -s tests -v