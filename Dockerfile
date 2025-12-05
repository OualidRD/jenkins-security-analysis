FROM python:3.11-slim

WORKDIR /app

# Copie des dépendances
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY bad/ ./bad/
COPY good/ ./good/

# Initialisation de la base de données (optional)
# RUN python bad/db_init.py || true

EXPOSE 5000

# Par défaut, lance l'app "bad" pour les analyses
CMD ["python", "-m", "bad.app"]
