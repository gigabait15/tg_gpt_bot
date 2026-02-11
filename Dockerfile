FROM python:3.12-slim


ENV PYTHONUNBUFFERED=1

ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml

RUN uv sync --frozen --no-dev

COPY . .

EXPOSE 8000

CMD ["uv","-n", "run","python", "-m", "main"]