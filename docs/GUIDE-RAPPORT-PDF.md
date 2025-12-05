# 📝 GUIDE POUR CRÉER LE RAPPORT PDF - Modèle à Suivre

Ce guide vous montre comment structurer votre rapport PDF, inspiré du rapport de votre collègue.

---

## 📋 Structure Recommandée du Rapport PDF

### 1. **Page de Titre** (1 page)

```
╔═══════════════════════════════════════════════════╗
║                                                   ║
║        ANALYSE DE SÉCURITÉ DES APPLICATIONS       ║
║              SAST - BANDIT vs TRIVY               ║
║                                                   ║
║                 PIPELINE JENKINS                  ║
║                                                   ║
║                                                   ║
║            Votre Nom                              ║
║            École/Université                       ║
║            Cours: Sécurité des Systèmes           ║
║            Date: Décembre 2024                    ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
```

**À inclure:**
- Titre du projet
- Votre nom et établissement
- Date
- Logos (école, Jenkins, Bandit, Trivy)

---

### 2. **Table des Matières** (1 page)

```
TABLE DES MATIÈRES
1. Résumé Exécutif                          Page 3
2. Introduction                              Page 4
3. Architecture et Configuration             Page 5
4. Outils et Technologies                    Page 7
5. Analyse SAST (Bandit)                    Page 8
6. Analyse SCA (Trivy)                      Page 12
7. Résultats et Comparaison                 Page 15
8. Recommandations de Sécurité              Page 18
9. Conclusion                                Page 20
10. Annexes                                  Page 21
    - A. Configuration Docker
    - B. Pipeline Jenkinsfile
    - C. Captures d'écran
```

---

### 3. **Résumé Exécutif** (1-2 pages)

```
RÉSUMÉ EXÉCUTIF

Objectif du Projet:
───────────────────
Démontrer les capacités d'analyse de sécurité applicative (SAST/SCA)
en utilisant une approche CI/CD automatisée avec Jenkins.

Résultats Principaux:
─────────────────────
✓ Code vulnérable analysé: 22 vulnérabilités détectées
✓ Code corrigé: 11 vulnérabilités restantes (50% d'amélioration)
✓ Dépendances scannées: 32+ packages
✓ CVE critiques identifiées: [Nombre exact après scan]

Livrables:
──────────
✓ Code source vulnérable (bad/) avec 10+ types de CWE
✓ Code source corrigé (good/) avec bonnes pratiques
✓ Pipeline Jenkins automatisé (9 stages)
✓ Rapports SAST en HTML et JSON
✓ Rapports SCA en JSON
✓ Documentation complète (README, QUICK-START)
✓ Conteneurisation Docker
```

---

### 4. **Introduction** (1 page)

```
INTRODUCTION

Contexte:
─────────
La sécurité des applications est devenue critique dans le développement
logiciel moderne. Les vulnérabilités non détectées peuvent conduire à
des compromissions graves.

Deux approches principales existent:
- SAST (Static Application Security Testing): Analyse le code source
- SCA (Software Composition Analysis): Analyse les dépendances

Objectif:
─────────
Mettre en place une chaîne complète d'analyse de sécurité intégrée au
pipeline CI/CD avec Jenkins.

Portée:
───────
✓ Analyse SAST avec Bandit
✓ Analyse SCA avec Trivy
✓ Comparaison code vulnérable vs corrigé
✓ Génération de rapports détaillés
✓ Documentation des vulnérabilités
```

---

### 5. **Architecture et Configuration** (2-3 pages)

#### 5.1 Architecture Générale

```
┌─────────────────────────────────────────────────────────────┐
│                    JENKINS PIPELINE                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │  SAST    │  │  SAST    │  │   SCA    │  │   SCA    │    │
│  │ Bandit   │→ │ Bandit   │→ │  Trivy   │→ │  Trivy   │    │
│  │  bad/    │  │  good/   │  │  deps    │  │  docker  │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
│       ↓              ↓              ↓              ↓          │
│  ┌──────────────────────────────────────────────────────┐   │
│  │        RAPPORTS (HTML + JSON)                        │   │
│  │   - bandit-bad.html                                  │   │
│  │   - bandit-good.html                                 │   │
│  │   - trivy-requirements.json                          │   │
│  │   - trivy-docker.json                                │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

À inclure:
- Diagramme Docker Compose
- Flux d'exécution pipeline
- Dépendances entre services

#### 5.2 Structure des Dossiers

```
jenkins-security-analysis/
├── bad/                    # Code vulnérable (pédagogique)
│   ├── app.py             # Flask avec vulnerabilités
│   ├── vulnerable_code.py # CWE/OWASP examples
│   └── db_init.py         # Init BD avec risques
│
├── good/                   # Code sécurisé (corrections)
│   ├── app.py             # Flask sécurisé
│   └── secure_code.py     # Code remédié
│
├── Jenkinsfile            # Pipeline 9 stages
├── docker-compose.yml     # Orchestration
├── Dockerfile             # App image
└── requirements.txt       # Dépendances
```

#### 5.3 Technologies Utilisées

| Composant | Technologie | Version | Rôle |
|-----------|-------------|---------|------|
| Langage | Python | 3.11 | Application |
| Framework | Flask | 3.1.2 | API web |
| CI/CD | Jenkins | LTS | Pipeline |
| SAST | Bandit | 1.8.6 | Analyse code |
| SCA | Trivy | 0.48.0 | Analyse dépendances |
| Conteneur | Docker | Latest | Déploiement |
| Orchestration | Docker Compose | Latest | Gestion services |

---

### 6. **Analyse SAST (Bandit)** (3-4 pages)

#### 6.1 Vue d'ensemble Bandit

```
QU'EST-CE QUE BANDIT?
────────────────────
Bandit est un outil SAST (Static Application Security Testing) qui:
- Analyse le code source Python ligne par ligne
- Identifie les patterns de sécurité dangereux
- Produit des rapports détaillés (HTML, JSON, CSV)
- Classifie les vulnérabilités par sévérité
```

#### 6.2 Résultats sur Code Vulnérable (bad/)

```
RÉSULTATS BANDIT - CODE VULNÉRABLE
──────────────────────────────────

Fichiers analysés: 3
  - app.py (107 lignes)
  - vulnerable_code.py (120 lignes)
  - db_init.py (25 lignes)

Total des vulnérabilités: 22

Répartition par sévérité:
┌─────────────────────────────────────┐
│ 🔴 HIGH:     2 vulnérabilités       │
│ 🟡 MEDIUM:  14 vulnérabilités       │
│ 🟢 LOW:      6 vulnérabilités       │
└─────────────────────────────────────┘

Répartition par type:
┌──────────────────────────────────────────┐
│ B201 Flask Debug True           2        │
│ B608 Possible SQL Injection      1       │
│ B105 Hardcoded Password         3        │
│ B605 Start Process with Shell    2       │
│ B377 Temp File Creation          1       │
│ B311 Weak Random               2        │
│ B301 Pickle Usage              1        │
│ B307 Unsafe Eval               2        │
│ B110 Bare Except               5        │
│ B400 No Timeout                2        │
└──────────────────────────────────────────┘
```

À inclure:
- Capture d'écran du rapport HTML Bandit
- Liste des vulnérabilités avec CWE/OWASP

#### 6.3 Top 5 Vulnérabilités Critiques

```
1. CWE-89: SQL Injection
   ├─ Fichier: bad/app.py, ligne 45
   ├─ Sévérité: 🔴 HIGH
   ├─ Description: Concaténation directe dans requête SQL
   └─ Impact: Accès/modification/suppression de données

2. CWE-94: Flask Debug Mode
   ├─ Fichier: bad/app.py, ligne 10
   ├─ Sévérité: 🔴 HIGH
   ├─ Description: app.run(debug=True) en production
   └─ Impact: Console interactive, révèle architecture

3. CWE-259: Hardcoded Password
   ├─ Fichier: bad/vulnerable_code.py, ligne 7
   ├─ Sévérité: 🟡 MEDIUM
   ├─ Description: Secrets en dur dans le code
   └─ Impact: Compromission des credentials

[etc...]
```

#### 6.4 Résultats sur Code Corrigé (good/)

```
RÉSULTATS BANDIT - CODE CORRIGÉ
───────────────────────────────

Total des vulnérabilités: 11 (50% réduction)

Répartition par sévérité:
┌─────────────────────────────────────┐
│ 🔴 HIGH:     0 vulnérabilités       │
│ 🟡 MEDIUM:   6 vulnérabilités       │
│ 🟢 LOW:      5 vulnérabilités       │
└─────────────────────────────────────┘

Vulnérabilités résiduelles:
- Mainly LOW severity (info/warnings)
- Pas de HIGH severity
- MEDIUM restantes (analyse false-positives)
```

---

### 7. **Analyse SCA (Trivy)** (2-3 pages)

#### 7.1 Vue d'ensemble Trivy

```
QU'EST-CE QUE TRIVY?
──────────────────
Trivy est un outil SCA (Software Composition Analysis) qui:
- Scanne les dépendances pour CVE connues
- Analyse les fichiers de configuration
- Détecte les secrets hardcodés
- Produit des rapports détaillés (JSON, Table, SBOM)
```

#### 7.2 Dépendances Analysées

```
DÉPENDANCES DIRECTES
────────────────────
Flask==3.1.2
  ├─ Werkzeug==3.0.1
  ├─ Jinja2==3.1.2
  └─ Click==8.1.7

requests==2.32.5
  ├─ urllib3==2.1.0
  ├─ certifi==2024.2.2
  └─ charset-normalizer==3.3.2

cryptography==46.0.3
PyJWT==2.10.1
Werkzeug==3.0.1

DÉPENDANCES TRANSITIVES: [List complète]

TOTAL: 32+ packages
```

#### 7.3 CVE Détectées

```
RÉSULTATS TRIVY - DÉPENDANCES
──────────────────────────────

CVE Trouvées:
┌────────────────────────────────────┐
│ 🔴 CRITICAL:     [X] CVE           │
│ 🟠 HIGH:         [Y] CVE           │
│ 🟡 MEDIUM:       [Z] CVE           │
│ 🟢 LOW:          [W] CVE           │
└────────────────────────────────────┘

Exemple de CVE:
├─ CVE-2024-XXXXX: Flask vulnerability
│  └─ Versions affectées: < 3.1.0
│  └─ Status: Not affected (version 3.1.2)
│
└─ CVE-2024-YYYYY: urllib3 issue
   └─ Versions affectées: < 2.0.0
   └─ Status: Not affected (version 2.1.0)
```

#### 7.4 Scan de l'Image Docker

```
RÉSULTATS TRIVY - IMAGE DOCKER
───────────────────────────────

Image: vulpy-app:local
  ├─ Base: python:3.11-slim
  ├─ Taille: ~150MB
  ├─ Couches: 15
  └─ CVE OS trouvées: [X]

CVE dans système d'exploitation:
[Lister les CVE pertinentes]
```

---

### 8. **Comparaison et Recommandations** (2 pages)

#### 8.1 Tableau Comparatif

| Aspect | bad/ | good/ | Amélioration |
|--------|------|-------|--------------|
| **SAST Issues** | 22 | 11 | -50% ✅ |
| **HIGH Severity** | 2 | 0 | -100% ✅ |
| **Code Quality** | Faible | Bon | Bien ✅ |
| **Secrets** | Hardcodés | Env vars | Sécurisé ✅ |
| **Errors** | Non gérés | Try/except | Robuste ✅ |
| **SQL** | Direct concat | Parameterized | Safe ✅ |

#### 8.2 Recommandations

```
RECOMMANDATIONS DE SÉCURITÉ
────────────────────────────

1. IMMÉDIAT (Sévérité: 🔴 HIGH)
   □ Désactiver le mode debug Flask
   □ Corriger les injections SQL
   □ Sécuriser les secrets

2. COURT TERME (Sévérité: 🟡 MEDIUM)
   □ Implémenter SAST dans le CI/CD
   □ Ajouter tests de sécurité
   □ Formaliser les revues de code

3. LONG TERME (Sévérité: 🟢 LOW)
   □ Intégrer SCA continu
   □ Former l'équipe à la sécurité
   □ Mettre en place DAST
```

---

### 9. **Conclusion** (1 page)

```
CONCLUSION

Résumé des Accomplissements:
─────────────────────────────
✅ Pipeline SAST/SCA complet et automatisé
✅ 22 vulnérabilités identifiées et documentées
✅ Code corrigé avec bonnes pratiques
✅ Rapports détaillés générés
✅ Infrastructure Docker en place

Leçons Apprises:
────────────────
1. L'automatisation est essentielle pour maintenir la sécurité
2. La détection précoce réduit les coûts de remédiation
3. Les bonnes pratiques doivent être documentées
4. L'analyse continue est plus efficace que ponctuelle

Perspectives Futures:
──────────────────
- Intégrer DAST (Analyse dynamique)
- Ajouter tests de pénétration
- Implémenter dans un vrai projet
- Élargir la couverture de sécurité
```

---

### 10. **Annexes** (2-3 pages)

#### Annexe A: Configuration Docker

```
DOCKERFILE
──────────
[Insérer le contenu du Dockerfile]

DOCKER-COMPOSE.YML
──────────────────
[Insérer le contenu du docker-compose.yml]
```

#### Annexe B: Pipeline Jenkins

```
JENKINSFILE (extrait)
─────────────────────
[Insérer les 20 premières lignes]

[Le fichier complet disponible à:
 jenkins-security-analysis/Jenkinsfile]
```

#### Annexe C: Captures d'écran

À inclure:
- [ ] Page d'accueil Jenkins
- [ ] Pipeline en cours d'exécution
- [ ] Résultats Bandit (bad/) HTML
- [ ] Résultats Bandit (good/) HTML
- [ ] Résultats Trivy (graphique)
- [ ] Logs du build Jenkins

#### Annexe D: Glossaire

```
GLOSSAIRE
─────────

SAST: Static Application Security Testing
      - Analyse le code source sans l'exécuter

SCA: Software Composition Analysis
     - Analyse les dépendances et librairies

CVE: Common Vulnerabilities and Exposures
     - Numéro d'identifiant pour vulnérabilités

CWE: Common Weakness Enumeration
     - Classification des fautes de sécurité

SBOM: Software Bill of Materials
      - Inventaire des composants logiciels
```

---

## 🛠️ Outils pour Créer le PDF

### Option 1: Microsoft Word
1. Copier les sections ci-dessus dans Word
2. Ajouter les captures d'écran
3. Formater avec styles
4. Exporter en PDF

### Option 2: Google Docs
1. Créer un document collaboratif
2. Importer les images/captures
3. Partager et exporter en PDF

### Option 3: LaTeX (Professionnel)
```latex
\documentclass{report}
\usepackage{graphicx}
\usepackage{hyperref}

\title{Analyse de Sécurité SAST/SCA}
\author{Votre Nom}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
% [Contenu du rapport]
\end{document}
```

### Option 4: Markdown → PDF
Convertir ce fichier markdown en PDF avec Pandoc:
```bash
pandoc rapport.md -o rapport.pdf
```

---

## 📸 Captures d'Écran à Prendre

Placez-les dans `docs/captures/`:

1. **pipeline-overview.png**: Jenkins interface
2. **bandit-bad.png**: Rapport HTML bad/
3. **bandit-good.png**: Rapport HTML good/
4. **trivy-docker.png**: Résultats Trivy
5. **jenkins-log.png**: Console output
6. **docker-services.png**: Services en cours

---

## ✅ Checklist Rapport

- [ ] Titre et page de couverture
- [ ] Table des matières avec numérotation
- [ ] Résumé exécutif
- [ ] Introduction et contexte
- [ ] Architecture documentée
- [ ] Résultats SAST détaillés
- [ ] Résultats SCA détaillés
- [ ] Comparaison bad vs good
- [ ] Recommandations
- [ ] Conclusion
- [ ] Annexes (Docker, Pipeline, Screenshots)
- [ ] Glossaire des termes
- [ ] Numérotation des pages
- [ ] Références/Sources
- [ ] Format et mise en page cohérents

---

**Ce template peut servir de base pour votre rapport PDF!**
**Longueur estimée: 20-30 pages avec captures d'écran**
