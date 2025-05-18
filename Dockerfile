FROM nginx:latest
FROM gunicorn:latest
FROM python:latest
WORKDIR /btre-web
COPY . .
RUN python3 -m venv .venv  && \
    source .venv/bin/activate && \
    pip install -r requirements.txt && \
    python manage.py collectstatic && \
    python manage.py migrate
EXPOSE 80
EXPOSE 443
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "btre.wsgi:application"]