"""
Application Flask volontairement vulnérable
Démo SAST (Bandit) et SCA (Trivy)
"""
from flask import Flask, request, render_template_string
import sqlite3
import os
import tempfile
import random
import pickle
import subprocess

app = Flask(__name__)

# ⚠️ VULNÉRABILITÉ 1: Mode debug activé (CWE-94, B201)
app.config['DEBUG'] = True

# ⚠️ VULNÉRABILITÉ 2: Clé secrète en dur (CWE-259, B105)
app.config['SECRET_KEY'] = 'hardcoded_secret_key_12345'

# ⚠️ VULNÉRABILITÉ 3: Mot de passe en dur (CWE-259, B105)
DATABASE_PASSWORD = "admin123"
API_KEY = "secret_api_key_abc123"

@app.route('/')
def home():
    return '''
    <h1>🔓 Application Vulnérable - SAST/SCA Demo</h1>
    <p>Cette application contient volontairement des vulnérabilités pédagogiques.</p>
    <ul>
        <li><a href="/user/1">👤 Utilisateur (SQL Injection)</a></li>
        <li><a href="/temp">📁 Fichier temporaire non sécurisé</a></li>
        <li><a href="/random">🎲 Générateur aléatoire faible</a></li>
        <li><a href="/exec">⚙️ Exécution de commande</a></li>
        <li><a href="/pickle">📦 Désérialisation Pickle</a></li>
        <li><a href="/eval">🧮 Utilisation d'eval()</a></li>
    </ul>
    '''

# ⚠️ VULNÉRABILITÉ 4: SQL Injection (CWE-89, B608)
@app.route('/user/<user_id>')
def get_user(user_id):
    """SQL Injection vulnerability"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # DANGEREUX: Injection SQL directe
    query = f"SELECT * FROM users WHERE id = {user_id}"
    try:
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()
        return f"User: {user}"
    except Exception as e:
        return f"Error: {str(e)}"

# ⚠️ VULNÉRABILITÉ 5: Fichier temporaire non sécurisé (CWE-377, B108)
@app.route('/temp')
def create_temp():
    """Insecure temporary file creation"""
    
    # DANGEREUX: Utilisation de /tmp directe
    temp_file = "/tmp/myfile_" + str(random.randint(0, 1000)) + ".txt"
    try:
        with open(temp_file, 'w') as f:
            f.write("données sensibles: " + DATABASE_PASSWORD)
        return f"Fichier créé: {temp_file}"
    except Exception as e:
        return f"Error: {str(e)}"

# ⚠️ VULNÉRABILITÉ 6: Générateur aléatoire faible (CWE-330, B311)
@app.route('/random')
def generate_random():
    """Weak random number generation"""
    
    # DANGEREUX: random.randint() n'est pas cryptographiquement sûr
    token = random.randint(1000, 9999)
    return f"Token (faible): {token}"

# ⚠️ VULNÉRABILITÉ 7: Exécution de commande (CWE-78, B605)
@app.route('/exec')
def execute_cmd():
    """Command injection vulnerability"""
    filename = request.args.get('file', 'test.txt')
    
    # DANGEREUX: Injection de commande
    try:
        result = os.system(f"cat {filename}")
        return f"Commande exécutée: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

# ⚠️ VULNÉRABILITÉ 8: Désérialisation Pickle (CWE-502, B301)
@app.route('/pickle')
def deserialize_pickle():
    """Unsafe pickle deserialization"""
    data = request.args.get('data', '').encode('latin1')
    
    try:
        # DANGEREUX: pickle.loads() avec données untrusted
        result = pickle.loads(data)
        return f"Résultat: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

# ⚠️ VULNÉRABILITÉ 9: Utilisation d'eval() (CWE-95, B307)
@app.route('/eval')
def evaluate():
    """Unsafe use of eval()"""
    expr = request.args.get('expr', '1+1')
    
    try:
        # DANGEREUX: eval() avec données untrusted
        result = eval(expr)
        return f"Résultat: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

# ⚠️ VULNÉRABILITÉ 10: Try/Except trop large (CWE-703, B110)
@app.route('/risky')
def risky_operation():
    """Bare exception handling"""
    try:
        # Opération dangereuse
        dangerous_func()
        return "OK"
    except:  # DANGEREUX: exception bare
        pass
    return "Erreur silencieuse"

def dangerous_func():
    raise Exception("Danger!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # ⚠️ B201
