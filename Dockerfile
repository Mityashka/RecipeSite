FROM python:3.10

RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean

RUN pip install poetry

WORKDIR /recipe_site

COPY pyproject.toml poetry.lock /recipe_site/

RUN poetry config virtualenvs.create false \
    && poetry install --only main

COPY recipe_site /recipe_site/

RUN python manage.py collectstatic --noinput

CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "recipe_site.wsgi:application"]