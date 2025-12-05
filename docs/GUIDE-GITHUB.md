# 🌐 GUIDE GITHUB - Pousser le Projet en Ligne

Ce guide explique comment mettre votre projet sur GitHub.

---

## 📋 Prérequis

- [ ] Compte GitHub créé (gratuit sur https://github.com)
- [ ] Git installé sur votre PC
- [ ] Docker Desktop configuré

---

## 🚀 Étapes pour Pousser sur GitHub

### Étape 1: Vérifier que Git est Installé

```powershell
git --version
```

Résultat attendu:
```
git version 2.xx.x.windows.x
```

Si non installé: Télécharger depuis https://git-scm.com/

---

### Étape 2: Configurer Git (Première fois)

```powershell
git config --global user.name "Votre Nom"
git config --global user.email "votre-email@example.com"

# Vérifier la configuration
git config --global user.name
git config --global user.email
```

---

### Étape 3: Créer un Repository sur GitHub

1. Aller sur https://github.com/new
2. **Repository name:** `jenkins-security-analysis`
3. **Description:** `Complete SAST/SCA analysis pipeline with Jenkins, Bandit and Trivy`
4. **Visibility:** Public (ou Private si préféré)
5. **Ne pas cocher:** "Initialize this repository with a README"
6. Cliquer: **Create repository**

Vous obtiendrez une URL comme:
```
https://github.com/votre-username/jenkins-security-analysis.git
```

---

### Étape 4: Initialiser Git Localement

```powershell
cd C:\Users\ouali\jenkins-security-analysis

# Initialiser le repo
git init

# Ajouter tous les fichiers (sauf ceux dans .gitignore)
git add .

# Vérifier ce qui sera commité
git status
```

Résultat attendu:
```
On branch master

No commits yet

Changes to be added:
  new file:   .gitignore
  new file:   README.md
  new file:   QUICK-START.md
  new file:   Jenkinsfile
  new file:   docker-compose.yml
  new file:   Dockerfile
  ...
  [liste de fichiers]
```

---

### Étape 5: Premier Commit

```powershell
git commit -m "Initial commit: Complete SAST/SCA analysis project structure

- Added vulnerable code (bad/) with 10+ CWE examples
- Added secured code (good/) with best practices
- Created Jenkins pipeline with SAST/SCA stages
- Configured Docker for application and Jenkins
- Added comprehensive documentation (README, QUICK-START)
- Created comparison guide (bad vs good)
- Ready for GitHub deployment"
```

---

### Étape 6: Ajouter le Repository Remote

```powershell
# Remplacer YOUR-USERNAME par votre username GitHub
git remote add origin https://github.com/YOUR-USERNAME/jenkins-security-analysis.git

# Vérifier
git remote -v
```

Résultat attendu:
```
origin  https://github.com/YOUR-USERNAME/jenkins-security-analysis.git (fetch)
origin  https://github.com/YOUR-USERNAME/jenkins-security-analysis.git (push)
```

---

### Étape 7: Pousser vers GitHub

```powershell
# Renommer la branche (Git utilise 'master' par défaut, GitHub utilise 'main')
git branch -M main

# Pousser
git push -u origin main
```

À la première tentative, une fenêtre d'authentification s'ouvrira:
- Option 1: Entrer vos credentials GitHub
- Option 2: Créer un Personal Access Token sur GitHub

**Recommandé: Utiliser un Personal Access Token**

---

## 🔐 Créer un Personal Access Token (Recommandé)

### Pour GitHub (non 2FA):

1. Aller sur: https://github.com/settings/tokens
2. Cliquer: **Generate new token**
3. **Token name:** `jenkins-security-analysis`
4. **Expiration:** 90 days (ou Never)
5. **Scopes:** Cocher `repo` et `workflow`
6. Cliquer: **Generate token**
7. **Copier le token** (vous ne le verrez plus)

### Utiliser le Token:

```powershell
git config --global credential.helper wincred

# Lors du push, utiliser:
# Username: votre-username
# Password: [Coller le token]
```

Ou directement dans l'URL:
```powershell
git remote set-url origin https://YOUR-USERNAME:YOUR-TOKEN@github.com/YOUR-USERNAME/jenkins-security-analysis.git
git push -u origin main
```

---

## ✅ Vérifier le Push

Aller sur GitHub:
```
https://github.com/YOUR-USERNAME/jenkins-security-analysis
```

Vous devez voir:
- ✅ Fichiers du projet
- ✅ README.md s'affiche en bas
- ✅ `.gitignore` fonctionne (pas de `reports/`, `__pycache__/`, etc.)
- ✅ Historique Git avec votre commit

---

## 📝 Ajouter une Description GitHub

1. Aller sur votre repository
2. Cliquer sur **⚙️ Settings**
3. Scrolldown jusqu'à **Description**
4. Ajouter:

```
Complete SAST/SCA security analysis pipeline for educational purposes.
Demonstrates secure vs vulnerable code with Jenkins CI/CD automation.

Features:
✅ SAST analysis with Bandit (bad/ vs good/ code)
✅ SCA analysis with Trivy (dependencies & Docker image)
✅ Automated Jenkins pipeline (9 stages)
✅ Docker containerization
✅ Comprehensive documentation
```

---

## 🌟 Ajouter un Badge README

Modifier `README.md` pour ajouter des badges:

```markdown
# 🔐 Jenkins Security Analysis

[![GitHub](https://img.shields.io/badge/GitHub-jenkins--security--analysis-blue?logo=github)](https://github.com/YOUR-USERNAME/jenkins-security-analysis)
[![License](https://img.shields.io/badge/License-Educational-green)](#)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue?logo=docker)](#)
[![Jenkins](https://img.shields.io/badge/Jenkins-LTS-red?logo=jenkins)](#)

> Complete SAST/SCA analysis pipeline for security-aware development
```

Puis pusher la modification:

```powershell
git add README.md
git commit -m "Add badges to README"
git push
```

---

## 📌 Ajouter des Topics GitHub

1. Sur GitHub: Repository → **⚙️ Settings**
2. Scrolldown: **Topics**
3. Ajouter:
   - `security`
   - `sast`
   - `sca`
   - `jenkins`
   - `bandit`
   - `trivy`
   - `docker`
   - `pipeline`
   - `cwe`
   - `vulnerability`
   - `education`

---

## 🔄 Mises à Jour Futures

Après chaque modification, pousser:

```powershell
cd C:\Users\ouali\jenkins-security-analysis

# Voir les modifications
git status

# Ajouter les fichiers modifiés
git add .

# Commit avec message descriptif
git commit -m "Description de la modification"

# Pousser
git push
```

---

## 📚 Branching (Optionnel)

Pour travailler sur des modifications sans affecter `main`:

```powershell
# Créer une nouvelle branche
git checkout -b feature/enhance-documentation

# Faire vos modifications...

# Pousser la branche
git push -u origin feature/enhance-documentation

# Sur GitHub: Créer une Pull Request (PR)
# Reviewer → Merge vers main
```

---

## 🏷️ Créer des Releases (Optionnel)

```powershell
# Créer un tag
git tag -a v1.0.0 -m "Initial release: SAST/SCA project"

# Pousser le tag
git push origin v1.0.0

# Sur GitHub: Aller à "Releases" → "Create Release from tag"
```

---

## 📊 Statistiques GitHub

Une fois poussé, GitHub affiche:
- **Stars:** Nombre d'utilisateurs qui likent votre projet
- **Forks:** Copies du projet par d'autres
- **Watchers:** Utilisateurs qui suivent les mises à jour
- **Issues:** Problèmes signalés
- **Discussions:** Conversations

---

## 🔒 Sécuriser votre Repository

### Paramètres de Sécurité:

1. **Settings → Security and analysis**
   - ✅ Enable: Dependabot alerts
   - ✅ Enable: Dependabot security updates
   - ✅ Enable: Secret scanning (Paid feature)

2. **Settings → Branch protection rules**
   - Créer une règle pour `main`:
     - ✅ Require pull request reviews
     - ✅ Require status checks to pass

---

## 📖 Partager votre Projet

### Lien Direct:
```
https://github.com/YOUR-USERNAME/jenkins-security-analysis
```

### Lien Avec Badge:
Ajouter au rapport PDF ou document:

```markdown
### Accès au Code Source

Le code source complet du projet est disponible sur GitHub:
https://github.com/YOUR-USERNAME/jenkins-security-analysis

Vous pouvez:
- ⭐ Star le project
- 🍴 Fork pour l'utiliser
- 💬 Ouvrir des Issues
- 📝 Créer des Pull Requests
```

---

## 🧪 Intégrer GitHub et Jenkins (Optionnel)

Pour que Jenkins se déclenche automatiquement lors d'un push:

1. **Installer le plugin:** GitHub sur Jenkins
2. **Settings → Webhooks** sur GitHub:
   - URL: `http://votre-jenkins.com/github-webhook/`
   - Sélectionner: `Push events`
3. Jenkins déclenche automatiquement le build

---

## ✅ Checklist Final

Avant de soumettre votre travail:

- [ ] Tous les fichiers sur GitHub
- [ ] `.gitignore` fonctionne (pas de `reports/`, `__pycache__/`)
- [ ] README.md bien formaté
- [ ] Commits avec messages clairs
- [ ] Pas de secrets commitées
- [ ] Description et badges ajoutés
- [ ] Repository "Public" ou "Private" selon les besoins
- [ ] Lien URL prêt à partager

---

## 📞 Référence Rapide Git

```powershell
# Voir l'historique
git log --oneline

# Voir les différences
git diff

# Annuler une modification
git reset HEAD <fichier>

# Cloner un repository
git clone https://github.com/USER/REPO.git

# Voir l'état
git status

# Configurer le repo
git config --list

# Ajouter un fichier
git add <fichier>

# Commit
git commit -m "Message"

# Pousser
git push

# Tirer les mises à jour
git pull
```

---

**Bravo! Votre projet est maintenant sur GitHub! 🎉**

Vous pouvez:
- ✅ Le partager avec des collègues
- ✅ L'utiliser dans des entretiens
- ✅ Le mettre à jour facilement
- ✅ Collaborer avec d'autres
- ✅ L'inclure dans votre portfolio
