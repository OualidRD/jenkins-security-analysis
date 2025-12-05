"""
Application Flask sécurisée
Correction des vulnérabilités du code bad/
"""
from flask import Flask, request
import sqlite3
import os
from secrets import token_hex
import logging

app = Flask(__name__)

# ✅ CORRECTED: Clé secrète depuis variable d'environnement
app.config['DEBUG'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', token_hex(32))

# ✅ CORRECTED: Mots de passe depuis variables d'environnement
DATABASE_PASSWORD = os.environ.get('DB_PASSWORD', '')
API_KEY = os.environ.get('API_KEY', '')

# ✅ CORRECTED: Logging approprié
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return '''
    <h1>✅ Application Sécurisée - Correction des vulnérabilités</h1>
    <ul>
        <li><a href="/user/1">👤 Utilisateur (SQL Injection - CORRIGÉ)</a></li>
        <li><a href="/random">🎲 Générateur aléatoire (CORRIGÉ)</a></li>
    </ul>
    '''

# ✅ CORRECTED: SQL Injection - Utilisation de parameterized query
@app.route('/user/<user_id>')
def get_user(user_id):
    """Safe parameterized SQL query"""
    try:
        # Validation de l'input
        user_id = int(user_id)
        
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        # ✅ SAFE: Parameterized query
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return f"User: {user}"
        else:
            return "Utilisateur non trouvé"
    except ValueError:
        return "Erreur: user_id doit être un nombre", 400
    except Exception as e:
        logger.error(f"Database error: {e}")
        return "Erreur interne", 500

# ✅ CORRECTED: Générateur aléatoire sécurisé (CWE-330)
@app.route('/random')
def generate_random():
    """Cryptographically secure random token"""
    
    # ✅ SAFE: Utilisation de secrets pour la sécurité
    token = token_hex(16)
    return f"Token (sécurisé): {token}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
