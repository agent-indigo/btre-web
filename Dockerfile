FROM nginx:latest
FROM python:latest
WORKDIR /btre-web
COPY . .
RUN python -m venv .venv \\
    source .venv/bin/activate \\
    pip install -r requirements.txt \\
    python manage.py collectstatic \\
    mv -r static/* /usr/share/nginx/html \\
    rmdir static
EXPOSE 80
EXPOSE 443
EXPOSE 8000
CMD ["source", ".venv/bin/activate", "&&", "python", "manage.py", "runserver"]