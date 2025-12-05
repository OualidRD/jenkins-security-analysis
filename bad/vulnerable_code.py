"""
Fichier vulnérable de démonstration pour l'analyse SAST
Contient plusieurs types de vulnérabilités détectées par Bandit
"""
import os
import subprocess
import requests
import pickle
import tempfile

# ⚠️ VULNÉRABILITÉ 1: Hardcoded Password (CWE-259, B105)
DATABASE_PASSWORD = "admin@123"
ADMIN_PASSWORD = "password123"
API_SECRET_KEY = "secret_key_12345abcde"
DATABASE_URL = "postgresql://user:MyPassword123@localhost/mydb"

# ⚠️ VULNÉRABILITÉ 2: Command Injection (CWE-78, B605, B607)
def execute_command(user_input):
    """Dangerous command execution"""
    # DANGEREUX: Injection de commande
    os.system(f"ls -la {user_input}")
    os.system("ping " + user_input)
    subprocess.call("echo " + user_input, shell=True)

# ⚠️ VULNÉRABILITÉ 3: Sous-processus sans timeout (CWE-400, B605)
def call_api(url):
    """Unreliable external call"""
    # DANGEREUX: Pas de timeout
    response = requests.get(url)
    return response.text

# ⚠️ VULNÉRABILITÉ 4: Try/Except trop large (CWE-703, B110)
def process_data(data):
    """Overly broad exception handling"""
    try:
        result = risky_operation(data)
        dangerous_db_query(data)
        another_risky_function(data)
    except:  # DANGEREUX: Bare except
        pass
    return None

# ⚠️ VULNÉRABILITÉ 5: Utilisation de Pickle (CWE-502, B301)
def deserialize_user_data(data):
    """Unsafe pickle deserialization"""
    # DANGEREUX: pickle.loads() avec données untrusted
    user_object = pickle.loads(data)
    return user_object

# ⚠️ VULNÉRABILITÉ 6: Utilisation d'Eval (CWE-95, B307)
def evaluate_expression(expr):
    """Unsafe eval usage"""
    # DANGEREUX: eval() avec données untrusted
    result = eval(expr)
    return result

# ⚠️ VULNÉRABILITÉ 7: Fichier temporaire non sécurisé (CWE-377, B108)
def create_temp_file(data):
    """Insecure temporary file"""
    # DANGEREUX: Chemin prédictible
    temp_path = "/tmp/tempdata_" + str(os.getpid()) + ".txt"
    with open(temp_path, 'w') as f:
        f.write(data)
    return temp_path

# ⚠️ VULNÉRABILITÉ 8: SQL Injection (CWE-89, B608)
def dangerous_db_query(user_id):
    """SQL Injection vulnerability"""
    # DANGEREUX: Concaténation dans requête SQL
    query = "SELECT * FROM users WHERE id = " + user_id
    # cursor.execute(query)  # Pas de parameterized query
    return query

# ⚠️ VULNÉRABILITÉ 9: Random faible (CWE-330, B311)
import random

def generate_token():
    """Weak random generation"""
    # DANGEREUX: random.randint() n'est pas cryptographiquement sûr
    token = random.randint(100000, 999999)
    return str(token)

def generate_session_id():
    """Weak random for security"""
    # DANGEREUX: Pour la sécurité, utiliser secrets.randbits()
    session_id = random.getrandbits(32)
    return hex(session_id)

# ⚠️ VULNÉRABILITÉ 10: Configuration dangereuse (B201)
def start_debug_server():
    """Debug mode activated"""
    from flask import Flask
    app = Flask(__name__)
    
    # DANGEREUX: Debug=True en production
    app.run(debug=True)

# ⚠️ VULNÉRABILITÉ 11: Utilisation de Assert (CWE-703, B101)
def validate_user(user):
    """Using assert for validation"""
    # DANGEREUX: Les asserts peuvent être désactivés
    assert user is not None, "User cannot be None"
    assert user['admin'] == True, "User must be admin"

# ⚠️ VULNÉRABILITÉ 12: Start process avec shell (B607)
def run_command(cmd):
    """Start process with shell"""
    # DANGEREUX: Shell=True avec injection
    subprocess.Popen(cmd, shell=True)

# Placeholder functions
def risky_operation(data):
    return data

def another_risky_function(data):
    return data
