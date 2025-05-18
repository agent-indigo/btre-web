FROM python:latest
WORKDIR /btre-web
COPY . .
RUN python3 -m venv .venv
RUN source .venv/bin/activate && \
    pip install -r requirements.txt && \
    pip install gunicorn && \
    python manage.py collectstatic && \
    python manage.py migrate
EXPOSE 80
EXPOSE 443
EXPOSE 8000
CMD [".venv/bin/gunicorn", "--bind", "0.0.0.0:8000", "btre.wsgi:application"]