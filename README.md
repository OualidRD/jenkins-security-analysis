# 🔐 Projet d'Analyse de Sécurité - Jenkins SAST/SCA

## 📋 Description

Projet complet d'analyse de sécurité applicative combinant:
- **SAST** (Static Application Security Testing) avec **Bandit**
- **SCA** (Software Composition Analysis) avec **Trivy**
- Pipeline CI/CD automatisé avec **Jenkins**
- Application Flask intentionnellement vulnérable pour démonstration pédagogique

## 🎯 Objectifs du Projet

1. ✅ Analyser le code source pour détecter les vulnérabilités (SAST)
2. ✅ Identifier les CVE dans les dépendances (SCA)
3. ✅ Automatiser l'analyse dans un pipeline Jenkins
4. ✅ Générer des rapports détaillés HTML/JSON
5. ✅ Démontrer la remédiation des vulnérabilités
6. ✅ Documenter les bonnes pratiques de sécurité

## 🛠️ Technologies Utilisées

| Technologie | Version | Rôle |
|---|---|---|
| Python | 3.11 | Langage de programmation |
| Flask | 3.1.2 | Framework web |
| Jenkins | LTS | Orchestrateur CI/CD |
| Bandit | 1.8.6 | Scanner SAST |
| Trivy | 0.48.0 | Scanner SCA/SBOM |
| Docker | Latest | Conteneurisation |

## 📁 Structure du Projet

```
jenkins-security-analysis/
│
├── 📄 README.md                    # Ce fichier
├── 📄 Jenkinsfile                  # Pipeline Jenkins (SAST + SCA)
├── 📄 docker-compose.yml           # Orchestration Docker
├── 📄 Dockerfile                   # Image de l'application
├── 📄 Dockerfile.jenkins           # Image Jenkins personnalisée
├── 📄 requirements.txt             # Dépendances Python
├── 📄 .gitignore                   # Fichiers à ignorer
│
├── 📂 bad/                         # ⚠️ CODE VULNÉRABLE
│   ├── __init__.py
│   ├── app.py                      # Flask avec vulnerabilités
│   ├── vulnerable_code.py          # Code avec CWE/OWASP
│   └── db_init.py                  # DB init avec risques
│
├── 📂 good/                        # ✅ CODE CORRIGÉ
│   ├── __init__.py
│   ├── app.py                      # Flask sécurisé
│   └── secure_code.py              # Code remédié
│
├── 📂 reports/                     # 📊 RAPPORTS D'ANALYSE
│   ├── bandit-bad.html             # SAST: code vulnérable
│   ├── bandit-good.html            # SAST: code corrigé
│   ├── bandit-bad.json             # Données brutes
│   ├── trivy-requirements.json     # SCA: dépendances
│   ├── trivy-docker.json           # SCA: image Docker
│   └── all-deps.txt                # Liste complète
│
└── 📂 docs/                        # 📖 DOCUMENTATION
    ├── captures/                   # Screenshots
    │   ├── pipeline-overview.png
    │   └── bandit-results.png
    └── [Rapports PDF]

```

## 🚀 Installation et Lancement

### Prérequis

- ✅ Docker Desktop installé
- ✅ Git installé
- ✅ Ports 8080 et 50000 disponibles
- ✅ Au moins 4GB RAM libres

### Étape 1: Cloner le Projet

```powershell
# Windows PowerShell
git clone https://github.com/votre-username/jenkins-security-analysis.git
cd jenkins-security-analysis
```

### Étape 2: Arrêter l'Ancien Jenkins (si existant)

```powershell
# Si vous aviez jenkins-n en cours d'exécution
cd C:\Users\ouali\jenkins-n
docker-compose down
docker volume prune
```

### Étape 3: Construire l'Image Jenkins

```powershell
# Dans le nouveau projet
cd C:\Users\ouali\jenkins-security-analysis
docker-compose build
```

### Étape 4: Démarrer les Services

```powershell
docker-compose up -d

# Vérifier que le conteneur démarre
docker logs -f jenkins-security
```

### Étape 5: Accéder à Jenkins

```
URL: http://localhost:8080
```

**Récupérer le mot de passe initial:**
```powershell
docker exec jenkins-security cat /var/jenkins_home/secrets/initialAdminPassword
```

### Étape 6: Configuration Jenkins

1. Copier le mot de passe et le coller dans Jenkins
2. Installer les plugins recommandés
3. Créer un compte admin
4. Créer un nouveau job **Pipeline**
5. Configuration → Definition → Pipeline script from SCM
6. SCM: Git
7. Repository URL: `file:///project` (ou votre repo GitHub)
8. Script Path: `Jenkinsfile`

### Étape 7: Lancer le Pipeline

```
Jenkins → Build Now
```

## 📊 Résultats Attendus

### Analyse SAST (Bandit)

**Code VULNÉRABLE (bad/):**
- ⚠️ ~22 vulnérabilités détectées
- 🔴 2 HIGH severity
- 🟡 14 MEDIUM severity
- 🟢 6 LOW severity

**Code CORRIGÉ (good/):**
- ✅ ~11 vulnérabilités
- Réduction de 50%+

### Analyse SCA (Trivy)

- 📦 Dépendances scannées: 32+
- 🔴 CVE Critical: [À déterminer]
- 🟡 CVE High: [À déterminer]
- 🟢 CVE Medium/Low: [À déterminer]

## 🔍 Vulnérabilités Principales Analysées

| CWE | Type | Sévérité | Fichier | Correction |
|---|---|---|---|---|
| CWE-94 | Flask Debug Mode | 🔴 HIGH | bad/app.py | debug=False + envvar |
| CWE-89 | SQL Injection | 🔴 HIGH | bad/app.py | Parameterized queries |
| CWE-259 | Hardcoded Password | 🟡 MEDIUM | bad/vulnerable_code.py | Environment variables |
| CWE-78 | Command Injection | 🔴 HIGH | bad/vulnerable_code.py | Subprocess list + timeout |
| CWE-377 | Insecure Temp File | 🟡 MEDIUM | bad/app.py | tempfile.NamedTemporaryFile |
| CWE-330 | Weak Random | 🟡 MEDIUM | bad/app.py | secrets module |
| CWE-502 | Pickle Unsafe | 🟡 MEDIUM | bad/vulnerable_code.py | JSON instead |
| CWE-95 | Unsafe Eval | 🔴 HIGH | bad/app.py | Restricted dict |
| CWE-703 | Bare Except | 🟡 MEDIUM | bad/vulnerable_code.py | Specific exceptions |
| CWE-400 | Timeout Not Set | 🟡 MEDIUM | bad/vulnerable_code.py | timeout=10 |

## 📈 Utilisation des Rapports

### Rapports HTML (Viewables)

```powershell
# Ouvrir les rapports HTML
Start-Process "http://localhost:8080/job/[nom-job]/artifact/reports/bandit-bad.html"
Start-Process "http://localhost:8080/job/[nom-job]/artifact/reports/bandit-good.html"
```

### Rapports JSON (Programmables)

```bash
# Analyser les données JSON
cat reports/bandit-bad.json | jq '.results[] | {severity, test_id, issue_text}'

# Compter les vulnérabilités
jq '.results | length' reports/bandit-bad.json
```

## 🎓 Cas d'Usage Pédagogiques

### 1. Démonstration des Vulnérabilités

**Avant (bad/):**
```python
# SQL Injection
query = f"SELECT * FROM users WHERE id = {user_id}"
cursor.execute(query)
```

**Après (good/):**
```python
# Safe parameterized query
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
```

### 2. Pipeline Automatisé

Le pipeline Jenkins exécute automatiquement:
1. SAST sur code bad/
2. SAST sur code good/
3. Comparaison des résultats
4. SCA des dépendances
5. Build de l'image Docker
6. Scan de l'image
7. Génération de rapports

### 3. Génération de Rapports

Les rapports sont disponibles à:
```
Jenkins → [Build] → Artifacts → reports/
```

## 🔧 Commandes Utiles

### Docker

```powershell
# Voir les logs Jenkins
docker logs -f jenkins-security

# Accéder au bash Jenkins
docker exec -it jenkins-security bash

# Voir l'espace disque utilisé
docker system df
```

### Bandit

```bash
# Scan d'un dossier
bandit -r bad/ -f html -o report.html

# Format JSON
bandit -r bad/ -f json -o report.json

# Avec limite de sévérité
bandit -r bad/ -ll  # Low level et au-dessus
```

### Trivy

```bash
# Scan d'un dossier
trivy fs --format json --output report.json .

# Scan d'une image
trivy image vulpy-app:local

# Scan avec sévérité minimale
trivy fs --severity MEDIUM,HIGH .
```

## 🐳 Déploiement de l'Application (Optionnel)

### Lancer l'Application Vulnérable

```bash
docker run -p 5000:5000 vulpy-app:local
# Accédez à http://localhost:5000
```

### Lancer avec Code Sécurisé

```bash
docker run -p 5000:5000 -e SECRET_KEY=your-key vulpy-app:local python -m good.app
```

## 📚 Ressources d'Apprentissage

### Sécurité Applicative
- [OWASP Top 10 2023](https://owasp.org/www-project-top-ten/)
- [CWE/SANS Top 25](https://cwe.mitre.org/top25/)

### Outils
- [Bandit Documentation](https://bandit.readthedocs.io/)
- [Trivy Documentation](https://aquasecurity.github.io/trivy/)
- [OWASP Code Review Guide](https://owasp.org/www-project-code-review-guide/)

### Best Practices
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference/)
- [12-Factor App Security](https://12factor.net/)

## 👤 Informations du Projet

**Auteur**: Votre Nom  
**Établissement**: Cours de Sécurité des Systèmes d'Information  
**Date**: Décembre 2024  
**Objectif**: Démonstration pédagogique de SAST/SCA  

## ⚠️ Avertissement Important

```
🚨 CETTE APPLICATION CONTIENT VOLONTAIREMENT DES VULNÉRABILITÉS 🚨

✋ NE JAMAIS DÉPLOYER EN PRODUCTION
✋ NE PAS UTILISER COMME TEMPLATE POUR UNE VRAIE APPLICATION
✋ À USAGE PÉDAGOGIQUE UNIQUEMENT

Cette application est destinée à:
✅ Comprendre les vulnérabilités courantes
✅ Apprendre à utiliser les outils SAST/SCA
✅ Pratiquer les techniques de remédiation
✅ Analyser les bonnes pratiques de sécurité
```

## 📝 Licence

Ce projet est fourni à titre éducatif. Tous droits réservés.

## 📞 Support

Pour des questions ou des problèmes:
1. Vérifiez que Docker Desktop est en cours d'exécution
2. Consultez les logs Jenkins: `docker logs jenkins-security`
3. Vérifiez les ports disponibles: `netstat -ano`
4. Reconstruisez l'image: `docker-compose build --no-cache`

---

**Prêt à commencer?** Allez à la section [Installation et Lancement](#-installation-et-lancement)
