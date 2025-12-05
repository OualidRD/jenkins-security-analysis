# 🚀 GUIDE DE LANCEMENT RAPIDE

## ⚡ Démarrage en 5 minutes

### 1️⃣ Arrêter l'ancien Jenkins (jenkins-n)

```powershell
cd C:\Users\ouali\jenkins-n
docker-compose down
docker volume prune -f
```

### 2️⃣ Aller dans le nouveau projet

```powershell
cd C:\Users\ouali\jenkins-security-analysis
```

### 3️⃣ Construire l'image Jenkins

```powershell
docker-compose build
```

**Temps estimé:** 3-5 minutes (première fois)

### 4️⃣ Démarrer le conteneur

```powershell
docker-compose up -d
```

Vérifier que le service démarre:

```powershell
docker logs -f jenkins-security
```

Attendez que vous voyez:
```
Jenkins is fully up and running
```

### 5️⃣ Accéder à Jenkins

```
http://localhost:8080
```

Récupérer le mot de passe:

```powershell
docker exec jenkins-security cat /var/jenkins_home/secrets/initialAdminPassword
```

### 6️⃣ Configuration Initial (2 minutes)

1. Copier le mot de passe
2. Coller dans Jenkins
3. Cliquer "Continue"
4. Sélectionner "Install suggested plugins"
5. Créer compte admin
6. Terminer la configuration

### 7️⃣ Créer le Pipeline

**Menu Jenkins:**
- New Item
- Name: `Pipeline-SAST-SCA`
- Type: **Pipeline**
- OK

**Configuration:**
- Definition: **Pipeline script from SCM**
- SCM: **Git**
- Repository URL: `file:///project`
- Script Path: `Jenkinsfile`
- Save

### 8️⃣ Lancer le Pipeline

```
Jenkins → Pipeline-SAST-SCA → Build Now
```

**Durée:** 5-10 minutes pour la première exécution

---

## 📊 Consulter les Résultats

### Option 1: Depuis Jenkins UI

```
Build → Artifacts → reports/
```

### Option 2: Rapports HTML

```powershell
# Ouvrir avec le navigateur par défaut
Start-Process "C:\Users\ouali\jenkins-security-analysis\reports\bandit-bad.html"
Start-Process "C:\Users\ouali\jenkins-security-analysis\reports\bandit-good.html"
```

### Option 3: Depuis le Terminal

```bash
# Voir les résultats en JSON
cat reports/bandit-bad.json | jq '.results[]'

# Compter les vulnérabilités
jq '.results | length' reports/bandit-bad.json
```

---

## 🐛 Dépannage

### Jenkins ne démarre pas

```powershell
# Vérifier les logs
docker logs jenkins-security

# Vérifier que le port 8080 n'est pas utilisé
netstat -ano | findstr :8080

# Supprimer et reconstruire
docker-compose down -v
docker system prune -f
docker-compose build --no-cache
docker-compose up -d
```

### Bandit/Trivy n'est pas installé

```powershell
# Vérifier l'installation dans le conteneur
docker exec jenkins-security bandit --version
docker exec jenkins-security trivy --version

# Reconstruire si nécessaire
docker-compose build --no-cache Dockerfile.jenkins
```

### Pas de rapports générés

1. Vérifier les logs du build: `Console Output`
2. Vérifier que les fichiers existent dans le workspace
3. Vérifier les permissions des fichiers

---

## 📁 Structure Créée

```
C:\Users\ouali\jenkins-security-analysis\
├── bad/                          # Code vulnérable
│   ├── app.py                    # Flask avec vulnérabilités
│   ├── vulnerable_code.py        # Autres vulnérabilités
│   └── db_init.py                # Initialisation BD
│
├── good/                         # Code corrigé
│   ├── app.py                    # Flask sécurisé
│   └── secure_code.py            # Code remédié
│
├── reports/                      # Rapports générés ✨
│   ├── bandit-bad.html
│   ├── bandit-good.html
│   ├── trivy-requirements.json
│   ├── trivy-docker.json
│   └── all-deps.txt
│
├── Dockerfile                    # Image application
├── Dockerfile.jenkins            # Image Jenkins
├── docker-compose.yml            # Orchestration
├── Jenkinsfile                   # Pipeline
├── requirements.txt              # Dépendances
├── README.md                     # Documentation
└── .gitignore                    # Fichiers à ignorer
```

---

## ✅ Checklist Verification

Après le lancement:

- [ ] Jenkins est accessible à http://localhost:9090
- [ ] Le pipeline `Pipeline-SAST-SCA` est créé
- [ ] Le build termine avec succès
- [ ] Fichiers générés dans `reports/`:
  - [ ] bandit-bad.html
  - [ ] bandit-good.html
  - [ ] trivy-requirements.json
  - [ ] trivy-docker.json
  - [ ] all-deps.txt
- [ ] Rapports visibles dans Jenkins Artifacts
- [ ] Rapports HTML consultables localement

---

## 📞 Besoin d'aide?

1. **Logs Jenkins:** `docker logs -f jenkins-security`
2. **Logs Build:** Jenkins → Build → Console Output
3. **Vérifier les services:** `docker-compose ps`
4. **Redémarrer complètement:** `docker-compose restart`

---

**Vous êtes prêt! Lancez le build et consultez les rapports SAST/SCA!** 🎉
