# 🔗 RESSOURCES ET RÉFÉRENCES

Ce fichier contient tous les liens utiles pour votre projet.

---

## 📖 Documentation Officielle

### Outils Utilisés

| Outil | Lien | Description |
|-------|------|-------------|
| **Bandit** | https://bandit.readthedocs.io/ | SAST Scanner pour Python |
| **Trivy** | https://aquasecurity.github.io/trivy/ | SCA/Container Scanner |
| **Jenkins** | https://www.jenkins.io/doc/ | CI/CD Automation |
| **Docker** | https://docs.docker.com/ | Conteneurisation |
| **Python** | https://docs.python.org/3.11/ | Langage de programmation |
| **Flask** | https://flask.palletsprojects.com/ | Framework web Python |

---

## 🔐 Sécurité et Standards

### OWASP (Open Web Application Security Project)

| Ressource | Lien | Contenu |
|-----------|------|---------|
| **Top 10 2023** | https://owasp.org/www-project-top-ten/ | 10 vulnérabilités critiques |
| **Top 10 2021** | https://owasp.org/www-project-top-ten-v2021/ | Version précédente |
| **API Security** | https://owasp.org/www-project-api-security/ | Sécurité des API |
| **Mobile** | https://owasp.org/www-project-mobile-top-10/ | Top 10 Mobile |

### CWE (Common Weakness Enumeration)

| Ressource | Lien |
|-----------|------|
| **CWE Top 25** | https://cwe.mitre.org/top25/ |
| **CWE-89** (SQL Injection) | https://cwe.mitre.org/data/definitions/89.html |
| **CWE-94** (Debug Mode) | https://cwe.mitre.org/data/definitions/94.html |
| **CWE-259** (Hardcoded Secrets) | https://cwe.mitre.org/data/definitions/259.html |
| **CWE-78** (Injection) | https://cwe.mitre.org/data/definitions/78.html |

### CVE (Common Vulnerabilities and Exposures)

| Ressource | Lien |
|-----------|------|
| **CVE Search** | https://cve.mitre.org/ |
| **NVD (National Vulnerability Database)** | https://nvd.nist.gov/ |
| **Exploit Database** | https://www.exploit-db.com/ |

---

## 🛠️ Outils Complémentaires

### Analyse de Sécurité Supplémentaires

```
SAST (Code Source):
├─ Bandit (Python) ✅ Utilisé
├─ SonarQube (Multi-language)
├─ Checkmarx (Enterprise)
├─ Fortify (Commercial)
└─ Semgrep (Open source)

SCA (Dépendances):
├─ Trivy ✅ Utilisé
├─ Snyk
├─ Black Duck
├─ OWASP Dependency-Check
└─ GitHub Dependabot

DAST (Runtime):
├─ OWASP ZAP
├─ Burp Suite
├─ Acunetix
└─ NessusVulnerabilities

IaC (Infrastructure):
├─ Terraform Scan
├─ CloudSploit
└─ Scout Suite
```

### GitHub Tools

```
GitHub Security:
├─ Dependabot Alerts
├─ Code Scanning
├─ Secret Scanning
└─ Security Advisories

GitHub Actions:
├─ Security Linter
├─ SBOM Generator
└─ Container Scanning
```

---

## 📚 Tutoriels Recommandés

### Bandit

```
1. Introduction à Bandit
   https://github.com/PyCQA/bandit/blob/master/README.rst

2. Configuration Bandit
   https://bandit.readthedocs.io/en/latest/configuration.html

3. Plugins Bandit
   https://bandit.readthedocs.io/en/latest/plugins/index.html

4. Plugin List (Test IDs)
   https://bandit.readthedocs.io/en/latest/plugins/index.html#test-plugins
```

### Trivy

```
1. Getting Started
   https://aquasecurity.github.io/trivy/

2. Configuration
   https://aquasecurity.github.io/trivy/docs/advanced/configuration/

3. Scanning Filesystems
   https://aquasecurity.github.io/trivy/docs/vulnerability/scanning/filesystem/

4. Scanning Images
   https://aquasecurity.github.io/trivy/docs/image/scanning/
```

### Jenkins Pipeline

```
1. Pipeline Documentation
   https://www.jenkins.io/doc/book/pipeline/

2. Declarative Pipeline
   https://www.jenkins.io/doc/book/pipeline/syntax/

3. Scripted Pipeline
   https://www.jenkins.io/doc/book/pipeline/pipeline-as-code/

4. Blue Ocean (UI)
   https://www.jenkins.io/doc/book/blueocean/
```

---

## 🐳 Docker Essentials

```
Docker Documentation:
├─ Installation
│  └─ https://docs.docker.com/get-docker/
│
├─ Docker CLI
│  └─ https://docs.docker.com/engine/reference/commandline/
│
├─ Docker Compose
│  └─ https://docs.docker.com/compose/
│
├─ Networking
│  └─ https://docs.docker.com/network/
│
└─ Best Practices
   └─ https://docs.docker.com/develop/dev-best-practices/
```

---

## 👨‍💻 Ressources d'Apprentissage

### Plateformes

```
Coursera:
├─ Python for Everybody
├─ Google Cloud Security
└─ https://www.coursera.org/

Udemy:
├─ Complete Python Bootcamp
├─ Docker Mastery
├─ Jenkins Complete Guide
└─ https://www.udemy.com/

PluralSight:
├─ Secure Coding Practices
├─ DevSecOps Essentials
└─ https://www.pluralsight.com/

YouTube:
├─ Network Chuck (Docker, Security)
├─ Fireship (Web Development)
└─ Tech With Tim (Python)
```

### Livres Recommandés

```
Sécurité:
├─ "The Web Application Hacker's Handbook" - Stuttard & Pinto
├─ "OWASP Top 10" - OWASP
└─ "Web Security Testing Cookbook" - Stuttard

Python:
├─ "Fluent Python" - Luciano Ramalho
├─ "Effective Python" - Brett Slatkin
└─ "Python Crash Course" - Eric Matthes

DevOps:
├─ "The DevOps Handbook" - Kim, Behr, Spafford
├─ "The Phoenix Project" - Gene Kim
└─ "Infrastructure as Code" - Kief Morris
```

---

## 🌐 Communautés Utiles

```
Stack Overflow:
├─ Tags: python, security, bandit, trivy, jenkins, docker
├─ URL: https://stackoverflow.com/
└─ Questions spécifiques et réponses

GitHub Discussions:
├─ Bandit: https://github.com/PyCQA/bandit/discussions
├─ Trivy: https://github.com/aquasecurity/trivy/discussions
└─ Jenkins: https://github.com/jenkinsci/jenkins/discussions

Reddit:
├─ r/learnprogramming
├─ r/cybersecurity
├─ r/devops
└─ r/Docker

LinkedIn Groups:
├─ Security Engineering
├─ DevOps Professionals
├─ Application Security
└─ Python Developers
```

---

## 🔍 Références dans le Projet

### Fichiers Locaux

```
C:\Users\ouali\jenkins-security-analysis\

README.md
├─ Introduction complète
├─ Installation détaillée
└─ Ressources dans le projet

QUICK-START.md
├─ 5 minutes pour démarrer
└─ Dépannage rapide

docs/COMPARAISON-BAD-GOOD.md
├─ Vulnérabilités expliquées
├─ Code avant/après
└─ Bonnes pratiques

docs/GUIDE-RAPPORT-PDF.md
├─ Template rapport
├─ Structures d'écrit
└─ Checklist complète

docs/GUIDE-GITHUB.md
├─ Instructions Git
├─ Pousser sur GitHub
└─ Collaboration

docs/GUIDE-SÉCURITÉ.md (CE FICHIER)
├─ Ressources externes
├─ Standards et bonnes pratiques
└─ Outils complémentaires
```

---

## 🧪 Laboratoires en Ligne

### Apprentissage Interactif

```
OWASP WebGoat:
├─ Tutoriel de sécurité web
├─ Exercices pratiques
└─ https://owasp.org/www-project-webgoat/

OWASP Juice Shop:
├─ Application vulnerable
├─ CTF challenges
└─ https://owasp.org/www-project-juice-shop/

HackTheBox:
├─ Machines à hacker
├─ Challenges (Free + Pro)
└─ https://www.hackthebox.com/

TryHackMe:
├─ Cybersecurity training
├─ Interactive labs
└─ https://www.tryhackme.com/

PentesterLab:
├─ Web penetration testing
├─ Exercises et certifications
└─ https://pentesterlab.com/
```

---

## 🏆 Certifications Recommandées

```
Security:
├─ CEH (Certified Ethical Hacker)
├─ OSCP (Offensive Security Certified Professional)
├─ GWAPT (GIAC Web Application Penetration Tester)
└─ Security+ (CompTIA)

Development:
├─ CPA (Certified Python Associate)
├─ Python Institute certifications
└─ Google Cloud Certification

DevOps:
├─ AWS Certified DevOps Engineer
├─ Kubernetes Certified Administrator (CKA)
└─ HashiCorp Certified: Terraform Associate
```

---

## 📊 Tableaux de Comparaison d'Outils

### SAST Scanners

| Outil | Langage | Prix | Rapport | Integration |
|-------|---------|------|---------|-------------|
| Bandit | Python | Gratuit | HTML, JSON | ✅ Jenkins |
| SonarQube | Multi | Gratuit/Payant | Web UI | ✅ Yes |
| Semgrep | Multi | Gratuit/Payant | JSON | ✅ Yes |
| Checkmarx | Multi | Payant | Web UI | ✅ Yes |

### SCA Scanners

| Outil | Langages | Prix | CVE DB | Speed |
|-------|----------|------|--------|-------|
| Trivy | Multi | Gratuit | ✅ | ⚡⚡⚡ |
| Snyk | Multi | Gratuit/Payant | ✅ | ⚡⚡ |
| OWASP DC | Multi | Gratuit | ✅ | ⚡ |
| Dependabot | Multi | Gratuit (GitHub) | ✅ | ⚡⚡ |

---

## 💡 Tips & Tricks

### Bandit

```bash
# Configuration custom
cat .bandit
[bandit]
exclude_dirs = ['/tests']
tests = [B201, B301, B302, B303, B304, B305, B306]

# Ignorer une ligne
# nosec
dangerous_code()  # nosec

# Ignorer un fichier
# bandit: skip_file
```

### Trivy

```bash
# Scan multiple targets
trivy fs . --severity HIGH,CRITICAL

# Ignore CVE
trivy --skip-update --ignorefile .trivyignore

# Generate SBOM
trivy sbom docker://myimage
```

### Jenkins

```groovy
// Email on failure
post {
    failure {
        emailext(
            subject: "Build Failed",
            body: "Build failed",
            to: "email@example.com"
        )
    }
}

// Keep old builds
options {
    buildDiscarder(logRotator(numToKeepStr: '30'))
}
```

---

## 🚀 Prochains Défis

### Après ce projet

```
Level 1 - Consolidation:
├─ Ajouter d'autres outils (SonarQube, Checkmarx)
├─ Implémenter DAST avec OWASP ZAP
└─ Ajouter tests unitaires

Level 2 - Complexité:
├─ Multi-language scanning
├─ Cloud security (AWS, Azure)
├─ Container orchestration (Kubernetes)
└─ Infrastructure as Code scanning

Level 3 - Expertise:
├─ Threat modeling
├─ Red team exercises
├─ Security architecture
└─ Incident response planning
```

---

## 📞 Support et Aide

### Si Vous Bloquez

```
1. Vérifiez la documentation locale:
   ├─ README.md
   ├─ QUICK-START.md
   └─ docs/

2. Consultez les ressources:
   ├─ Official docs (liens ci-dessus)
   ├─ Stack Overflow
   └─ GitHub Issues

3. Essayez le dépannage:
   ├─ Logs détaillés (docker-compose logs -f)
   ├─ Nettoyer et redémarrer (docker system prune)
   └─ Reconstruire l'image (docker-compose build --no-cache)
```

---

## ✅ Checklist Apprentissage

- [ ] Comprendre SAST vs SCA
- [ ] Maîtriser Bandit (résultats, configuration)
- [ ] Maîtriser Trivy (scan filesystem, image, secrets)
- [ ] Comprendre CWE et CVE
- [ ] Configurer Jenkins pipeline
- [ ] Conteneuriser une application
- [ ] Intégrer Docker avec CI/CD
- [ ] Générer rapports de sécurité
- [ ] Corriger vulnérabilités
- [ ] Pousser sur GitHub

---

**Bonne chance dans votre parcours de sécurité!** 🎯

Pour plus d'informations, consultez les documentations officielles des outils utilisés.
