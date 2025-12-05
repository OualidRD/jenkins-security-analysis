# ⚡ CHEAT SHEET - Accès Rapide

## 🚀 Lancer le Projet (1 minute)

```powershell
# 1. Ouvrir Docker Desktop (attendre "running")

# 2. Terminal PowerShell
cd C:\Users\ouali\jenkins-security-analysis
docker-compose up -d

# 3. Accédez à Jenkins
# http://localhost:8080

# 4. Mot de passe
docker exec jenkins-security cat /var/jenkins_home/secrets/initialAdminPassword
```

---

## 📚 Fichiers Principaux

| Fichier | Lignes | Contenu |
|---------|--------|---------|
| **README.md** | 400+ | Documentation complète |
| **QUICK-START.md** | 200+ | Démarrage en 5 min |
| **RESUME-FINAL.md** | 300+ | Ce qui a été créé |
| **Jenkinsfile** | 250+ | Pipeline SAST/SCA |
| **bad/app.py** | 107 | Code vulnérable |
| **good/app.py** | 65 | Code sécurisé |

---

## 🔧 Commandes Git

```bash
# Initialiser
git init
git add .
git commit -m "Initial commit"

# Créer repository sur https://github.com/new

# Pousser
git remote add origin https://github.com/USERNAME/jenkins-security-analysis.git
git branch -M main
git push -u origin main
```

---

## 📊 Pipeline Jenkins

```
1. Bandit (bad/)      → 22 vulnérabilités
2. Bandit (good/)     → 11 vulnérabilités
3. Comparaison        → Stats
4. Trivy (deps)       → CVE dépendances
5. Trivy (supply)     → Scan complet
6. Trivy (docker)     → Scan image
7. Build Docker       → Image créée
8. Rapports           → HTML + JSON
```

---

## 📂 Structure

```
bad/                  - Code VULNÉRABLE (10+ CWE)
good/                 - Code SÉCURISÉ (corrections)
docs/                 - Documentation complète
reports/              - Rapports générés (gitignore)
Jenkinsfile           - Pipeline 8 stages
docker-compose.yml    - Configuration Docker
```

---

## 🎯 Top 10 Vulnérabilités

1. SQL Injection (CWE-89)
2. Debug Mode (CWE-94)
3. Hardcoded Secrets (CWE-259)
4. Command Injection (CWE-78)
5. Insecure Temp (CWE-377)
6. Weak Random (CWE-330)
7. Pickle Unsafe (CWE-502)
8. Unsafe Eval (CWE-95)
9. Bare Except (CWE-703)
10. No Timeout (CWE-400)

---

## 🔗 Liens Rapides

```
Jenkins:              http://localhost:9090
Bandit Docs:          https://bandit.readthedocs.io/
Trivy Docs:           https://aquasecurity.github.io/trivy/
OWASP Top 10:         https://owasp.org/www-project-top-ten/
CWE Database:         https://cwe.mitre.org/
```

---

## ❓ Dépannage Rapide

```powershell
# Jenkins ne démarre pas
docker-compose logs jenkins-security

# Port 8080 déjà utilisé
netstat -ano | findstr :8080
Stop-Process -Id [PID] -Force

# Nettoyer tout
docker system prune -f
docker volume prune -f

# Reconstruire
docker-compose build --no-cache
```

---

## 📋 Avant Soumission

- [ ] Pipeline exécuté ✅
- [ ] Rapports générés ✅
- [ ] Code poussé sur GitHub ✅
- [ ] Rapport PDF rédigé ✅
- [ ] README consulté ✅

---

**Besoin d'aide?** → Consultez `README.md` ou `QUICK-START.md`
