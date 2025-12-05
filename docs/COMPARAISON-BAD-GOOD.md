# 📊 TABLEAU DE COMPARAISON - BAD vs GOOD

Ce document montre la comparaison entre le code vulnérable et le code sécurisé.

---

## 🔴 Vulnérabilité 1: SQL Injection (CWE-89)

### ❌ Code Vulnérable (bad/app.py)

```python
@app.route('/user/<user_id>')
def get_user(user_id):
    # DANGEREUX: Injection SQL
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"  # ⚠️ RISQUE!
    cursor.execute(query)
    user = cursor.fetchone()
    return f"User: {user}"
```

**Risque:** Un attaquant peut modifier la requête:
```
/user/1 OR 1=1  → SELECT * FROM users WHERE id = 1 OR 1=1  (récupère tous)
/user/1; DROP TABLE users;  → Supprime la table
```

**Détection Bandit:** `B608: Possible SQL injection`

### ✅ Code Corrigé (good/app.py)

```python
@app.route('/user/<user_id>')
def get_user(user_id):
    try:
        # SÉCURISÉ: Parameterized query
        user_id = int(user_id)  # Validation
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))  # ✅ SAFE!
        user = cursor.fetchone()
        return f"User: {user}"
    except ValueError:
        return "Erreur: user_id doit être un nombre", 400
```

**Avantages:**
- ✅ Paramètre séparé de la requête
- ✅ Validation du type
- ✅ Gestion d'erreur appropriée

---

## 🔴 Vulnérabilité 2: Secrets en Dur (CWE-259)

### ❌ Code Vulnérable (bad/vulnerable_code.py)

```python
# DANGEREUX: Secrets en dur dans le code
DATABASE_PASSWORD = "admin@123"
API_SECRET_KEY = "secret_key_12345abcde"
DATABASE_URL = "postgresql://user:MyPassword123@localhost/mydb"
```

**Risque:** 
- Secrets visibles dans GitHub
- Difficile à changer en production
- Accès non contrôlé

**Détection Bandit:** `B105: hardcoded_password_string`  
**Détection Trivy:** Patterns de secrets dans code

### ✅ Code Corrigé (good/vulnerable_code.py)

```python
import os

# SÉCURISÉ: Secrets depuis variables d'environnement
DATABASE_PASSWORD = os.environ.get('DB_PASSWORD')
API_KEY = os.environ.get('API_KEY')

# Ou utiliser python-dotenv
from dotenv import load_dotenv
load_dotenv()
DB_URL = os.getenv('DATABASE_URL')
```

**Utilisation:**
```powershell
# Avant de lancer l'app
$env:DB_PASSWORD = "secure-password"
$env:API_KEY = "secret-key"
python app.py
```

**Avantages:**
- ✅ Secrets en dehors du code
- ✅ Facile à changer en production
- ✅ Pas commité sur GitHub

---

## 🔴 Vulnérabilité 3: Générateur Aléatoire Faible (CWE-330)

### ❌ Code Vulnérable (bad/app.py)

```python
import random

@app.route('/random')
def generate_random():
    # DANGEREUX: random.randint() n'est pas cryptographiquement sûr
    token = random.randint(1000, 9999)  # ⚠️ PRÉVISIBLE!
    return f"Token: {token}"
```

**Risque:**
- Plage très petite (10000 combinaisons)
- Facile à brute-force
- Prédictible

**Détection Bandit:** `B311: Use of random module`

### ✅ Code Corrigé (good/secure_code.py)

```python
from secrets import token_hex, randbits

def generate_token():
    # SÉCURISÉ: secrets.token_hex() pour tokens
    token = token_hex(32)  # 64 caractères hexadécimaux
    return token

def generate_session_id():
    # SÉCURISÉ: secrets.randbits() pour nombres
    session_id = secrets.randbits(256)  # 256-bit aléatoire
    return hex(session_id)
```

**Avantages:**
- ✅ Cryptographiquement sûr
- ✅ Basé sur l'entropy du système
- ✅ Impossible à prédire
- ✅ Plage énorme

---

## 🔴 Vulnérabilité 4: Injection de Commande (CWE-78)

### ❌ Code Vulnérable (bad/vulnerable_code.py)

```python
import os

def execute_command(user_input):
    # DANGEREUX: Injection de commande
    os.system(f"ls -la {user_input}")  # ⚠️ SHELL INJECTION!
```

**Risque:** Un attaquant peut faire:
```
execute_command("file.txt; rm -rf /")  
→ ls -la file.txt; rm -rf /  (supprime tout!)

execute_command("$(malicious_command)")
→ Exécute commande arbitraire
```

**Détection Bandit:** `B605: Start process with a shell`

### ✅ Code Corrigé (good/secure_code.py)

```python
import subprocess

def execute_command(user_input):
    # Whitelist de commandes autorisées
    allowed_commands = ['ls', 'pwd', 'date']
    
    if not any(cmd in user_input.lower() for cmd in allowed_commands):
        raise ValueError("Commande non autorisée")
    
    # SÉCURISÉ: Utiliser list, pas shell=True
    try:
        result = subprocess.run(
            user_input.split(),  # Liste, pas string!
            capture_output=True,
            text=True,
            timeout=5  # Timeout défini
        )
        return result.stdout
    except subprocess.TimeoutExpired:
        return "Timeout"
```

**Avantages:**
- ✅ Pas de shell (pas de `shell=True`)
- ✅ Whitelist de commandes
- ✅ Timeout défini (CWE-400)
- ✅ Pas d'expansion de caractères

---

## 🔴 Vulnérabilité 5: Mode Debug Activé (CWE-94)

### ❌ Code Vulnérable (bad/app.py)

```python
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True  # ⚠️ DANGEREUX!

if __name__ == '__main__':
    app.run(debug=True)  # ⚠️ CONSOLE INTERACTIVE!
```

**Risques:**
- Affiche l'exception complète (révèle l'architecture)
- Console Python interactive sur /console
- Recharge du code automatique
- Jeton PIN peut être contourné

**Détection Bandit:** `B201: flask_debug_true`

### ✅ Code Corrigé (good/app.py)

```python
from flask import Flask
import os

app = Flask(__name__)

# SÉCURISÉ: Debug depuis env variable
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False') == 'True'

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False  # ✅ Désactivé en production
    )
```

**Utilisation:**
```powershell
# En développement (optionnel)
$env:FLASK_DEBUG = "True"
python app.py

# En production (défaut)
python app.py  # debug=False
```

**Avantages:**
- ✅ Contrôlable via environment
- ✅ Désactivé par défaut
- ✅ Pas de console
- ✅ Messages d'erreur génériques

---

## 🔴 Vulnérabilité 6: Fichier Temporaire Non Sécurisé (CWE-377)

### ❌ Code Vulnérable (bad/app.py)

```python
@app.route('/temp')
def create_temp():
    # DANGEREUX: Chemin prédictible
    temp_file = "/tmp/myfile_" + str(os.getpid()) + ".txt"  # ⚠️ PRÉVISIBLE!
    with open(temp_file, 'w') as f:
        f.write("données sensibles")
    return f"Fichier créé: {temp_file}"
```

**Risque:** Race condition
- PID est prévisible
- Attaquant peut créer le fichier avant
- Lecture/modification possible
- Permissions faibles

### ✅ Code Corrigé (good/secure_code.py)

```python
import tempfile

def create_temp_file(data):
    # SÉCURISÉ: tempfile.NamedTemporaryFile
    with tempfile.NamedTemporaryFile(
        mode='w',
        delete=False,
        suffix='.txt',
        dir=tempfile.gettempdir()
    ) as f:
        f.write(data)
        return f.name
```

**Avantages:**
- ✅ Chemin cryptographiquement aléatoire
- ✅ Créé atomiquement
- ✅ Permissions restrictives
- ✅ Pas de race condition

---

## 🔴 Vulnérabilité 7: Désérialisation Unsafe (CWE-502)

### ❌ Code Vulnérable (bad/vulnerable_code.py)

```python
import pickle

def deserialize_user_data(data):
    # DANGEREUX: pickle.loads() avec données untrusted
    user_object = pickle.loads(data)  # ⚠️ ARBITRARY CODE EXECUTION!
    return user_object
```

**Risque:** Pickle peut exécuter du code arbitrary
```python
# Attaque
import pickle
import os
import pickletools

# Crée un objet malveillant
malicious = "cos\nsystem\n(S'rm -rf /'\ntR."
os.system("cat /etc/passwd")
# → Exécuté lors du unpickle!
```

**Détection Bandit:** `B301: Pickle usage`

### ✅ Code Corrigé (good/secure_code.py)

```python
import json

def deserialize_user_data(json_data):
    # SÉCURISÉ: JSON au lieu de Pickle
    try:
        user_object = json.loads(json_data)
        return user_object
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
        raise
```

**Avantages:**
- ✅ JSON ne peut pas exécuter de code
- ✅ Format standard et sûr
- ✅ Pas de code arbitraire
- ✅ Interopérable

---

## 🔴 Vulnérabilité 8: Utilisation d'Eval (CWE-95)

### ❌ Code Vulnérable (bad/vulnerable_code.py)

```python
def evaluate_expression(expr):
    # DANGEREUX: eval() avec données untrusted
    result = eval(expr)  # ⚠️ CODE EXECUTION!
    return result
```

**Risque:** Eval exécute n'importe quel code Python
```
evaluate_expression("__import__('os').system('rm -rf /')")
→ Supprime tout!

evaluate_expression("open('/etc/passwd').read()")
→ Lit fichiers système
```

**Détection Bandit:** `B307: Use of possibly insecure function`

### ✅ Code Corrigé (good/secure_code.py)

```python
def evaluate_expression(expr):
    # Whitelist d'opérations autorisées
    safe_dict = {
        'abs': abs,
        'round': round,
        'pow': pow
    }
    
    try:
        # SÉCURISÉ: eval() avec dictionnaire restreint
        result = eval(expr, {"__builtins__": {}}, safe_dict)
        return result
    except Exception as e:
        logger.error(f"Eval error: {e}")
        raise
```

**Utilisation:**
```python
evaluate_expression("abs(-5)")  # ✅ OK: 5
evaluate_expression("pow(2, 3)")  # ✅ OK: 8
evaluate_expression("__import__('os')")  # ❌ NameError (bloqué)
```

**Avantages:**
- ✅ Whitelist de fonctions
- ✅ Builtins désactivés
- ✅ Contrôle granulaire
- ✅ Exceptions explicites

---

## 📊 Résumé Comparatif

| Vulnérabilité | CWE | Sévérité | Détection | Correction |
|---|---|---|---|---|
| SQL Injection | CWE-89 | 🔴 HIGH | Bandit | Parameterized query |
| Secrets | CWE-259 | 🟡 MEDIUM | Bandit/Trivy | Env variables |
| Random faible | CWE-330 | 🟡 MEDIUM | Bandit | secrets module |
| Injection commande | CWE-78 | 🔴 HIGH | Bandit | subprocess list |
| Debug mode | CWE-94 | 🔴 HIGH | Bandit | debug=False |
| Temp file | CWE-377 | 🟡 MEDIUM | Bandit | tempfile module |
| Pickle unsafe | CWE-502 | 🟡 MEDIUM | Bandit | JSON format |
| Eval unsafe | CWE-95 | 🔴 HIGH | Bandit | Restricted dict |
| Bare except | CWE-703 | 🟡 MEDIUM | Bandit | Specific exceptions |
| No timeout | CWE-400 | 🟡 MEDIUM | Bandit | timeout param |

---

## ✅ Résultats Attendus Bandit

```
CODE VULNÉRABLE (bad/):
  Issues found: 22
  - HIGH: 2
  - MEDIUM: 14
  - LOW: 6

CODE CORRIGÉ (good/):
  Issues found: 11
  - HIGH: 0
  - MEDIUM: 6
  - LOW: 5

Amélioration: 50% de réduction
```

---

**Ce tableau peut être intégré directement dans votre rapport PDF!**
