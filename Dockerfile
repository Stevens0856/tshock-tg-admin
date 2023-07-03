FROM python:3.11.4-alpine3.18

ARG BUILD_TYPE=production

ENV BUILD_TYPE=${BUILD_TYPE} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.5.1

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install $(test "$BUILD_TYPE" == production && echo "--no-dev") --no-interaction --no-ansi --no-root

# Creating folders, and files for a project:
COPY . /code

CMD ["poetry", "run", "python", "main.py"]
