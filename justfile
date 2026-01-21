[private]
default:
    just --list

check: fmt lint test

test:
    uv run pytest

fmt:
    uv run ruff format
    uv run ruff check

lint:
    uv run ty check
    uv run mypy --strict anthropic_data tests

