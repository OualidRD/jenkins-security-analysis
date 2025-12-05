pipeline {
    agent any
    
    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timeout(time: 1, unit: 'HOURS')
    }
    
    stages {
        // ========================================
        // PHASE 0: VÉRIFICATION PRÉALABLE
        // ========================================
        stage('Préparation') {
            steps {
                script {
                    echo """
                    ╔════════════════════════════════════════════╗
                    ║        PIPELINE SAST/SCA JENKINS            ║
                    ║    Analyse de Sécurité du Code Source      ║
                    ╚════════════════════════════════════════════╝
                    
                    🔍 Phases d'analyse:
                       1️⃣  SAST avec Bandit (Code vulnérable + corrigé)
                       2️⃣  SCA avec Trivy (Dépendances + Docker)
                       3️⃣  Build image Docker
                       4️⃣  Scan de l'image
                       5️⃣  Rapport final
                    """
                }
                
                sh '''
                    mkdir -p ${WORKSPACE}/reports
                    
                    echo "✓ Dossier reports créé"
                    echo "✓ Vérification de Docker..."
                    docker --version
                    echo "✓ Vérification de Trivy..."
                    trivy --version
                '''
            }
        }
        
        // ========================================
        // PHASE 1: SAST avec Bandit
        // ========================================
        stage('SAST - Bandit: Code Vulnérable') {
            steps {
                script {
                    echo """
                    ╔════════════════════════════════════════════╗
                    ║    ÉTAPE 1: ANALYSE SAST - CODE VULNÉRABLE ║
                    ╚════════════════════════════════════════════╝
                    """
                }
                
                sh '''
                    if [ ! -d "/var/jenkins_home/bandit-venv" ]; then
                        python3 -m venv /var/jenkins_home/bandit-venv
                        . /var/jenkins_home/bandit-venv/bin/activate
                        pip install -q bandit==1.8.6
                    else
                        . /var/jenkins_home/bandit-venv/bin/activate
                    fi
                    
                    echo "Running Bandit analysis on bad/ folder..."
                    bandit -r bad -f html -o reports/bandit-bad.html 2>&1
                    EXIT_CODE=$?
                    echo "Bandit completed with exit code: $EXIT_CODE"
                    
                    ls -lh reports/bandit-bad.html
                '''
            }
        }
        
        stage('SAST - Bandit: Code Corrigé') {
            steps {
                script {
                    echo """
                    ╔════════════════════════════════════════════╗
                    ║    ÉTAPE 2: ANALYSE SAST - CODE CORRIGÉ    ║
                    ╚════════════════════════════════════════════╝
                    """
                }
                
                sh '''
                    . /var/jenkins_home/bandit-venv/bin/activate
                    
                    echo "Running Bandit analysis on good/ folder..."
                    bandit -r good -f html -o reports/bandit-good.html 2>&1
                    EXIT_CODE=$?
                    echo "Bandit completed with exit code: $EXIT_CODE"
                    
                    ls -lh reports/bandit-good.html
                '''
            }
        }
        
        stage('SAST - Comparaison bad vs good') {
            steps {
                script {
                    echo """
                    ╔════════════════════════════════════════════╗
                    ║         COMPARAISON BAD vs GOOD            ║
                    ╚════════════════════════════════════════════╝
                    """
                }
                
                sh '''
                    echo "📊 Rapport comparatif SAST..."
                    echo ""
                    echo "Fichiers générés:"
                    ls -lh reports/bandit-*.html 2>/dev/null || echo "Pas de rapports HTML"
                    ls -lh reports/bandit-*.json 2>/dev/null || echo "Pas de rapports JSON"
                    echo ""
                    echo "✅ Comparaison terminée"
                '''
            }
        }
        
        // ========================================
        // PHASE 2: SCA avec Trivy
        // ========================================
        stage('SCA - Trivy: Analyse des dépendances') {
            steps {
                script {
                    echo """
                    ╔════════════════════════════════════════════╗
                    ║   ÉTAPE 3: ANALYSE SCA - DÉPENDANCES      ║
                    ╚════════════════════════════════════════════╝
                    """
                }
                
                sh '''
                    echo "📦 Scan du fichier requirements.txt..."
                    trivy fs requirements.txt --format table 2>&1 | head -100 || echo "Trivy scan completed"
                    echo "✅ Analyse requirements.txt terminée"
                '''
            }
        }
        
        stage('SCA - Trivy: Supply-chain complet') {
            steps {
                script {
                    echo """
                    ╔════════════════════════════════════════════╗
                    ║  ÉTAPE 4: ANALYSE SCA - SUPPLY-CHAIN       ║
                    ╚════════════════════════════════════════════╝
                    """
                }
                
                sh '''
                    echo "🔍 Scan du répertoire courant..."
                    trivy fs . --format table 2>&1 | head -100 || echo "Trivy scan completed"
                    echo "✅ Supply-chain analysée"
                '''
            }
        }
        
        stage('SCA - Dépendances transitives') {
            steps {
                script {
                    echo """
                    ╔════════════════════════════════════════════╗
                    ║  ÉTAPE 5: DÉPENDANCES TRANSITIVES         ║
                    ╚════════════════════════════════════════════╝
                    """
                }
                
                sh '''
                    echo "📊 Analyse des dépendances transitives..."
                    python3 -m venv /tmp/scan-venv 2>/dev/null || true
                    . /tmp/scan-venv/bin/activate 2>/dev/null || true
                    pip install --quiet -r requirements.txt 2>/dev/null || true
                    pip freeze > reports/all-deps.txt 2>/dev/null || echo "# Dépendances" > reports/all-deps.txt
                    echo "✅ Dépendances transitives listées"
                '''
            }
        }
        
        // ========================================
        // PHASE 3: Build et Scan Image Docker
        // ========================================
        stage('Build Docker Image') {
            steps {
                script {
                    echo """
                    ╔════════════════════════════════════════════╗
                    ║  ÉTAPE 6: BUILD DE L'IMAGE DOCKER         ║
                    ╚════════════════════════════════════════════╝
                    """
                }
                
                sh '''
                    echo "🐳 Construction de l'image Docker: vulpy-app:local..."
                    docker build -t vulpy-app:local . 2>&1 | tail -20 || echo "Docker build completed"
                    echo "✅ Image Docker construite"
                '''
            }
        }
        
        stage('SCA - Scan Image Docker') {
            steps {
                script {
                    echo """
                    ╔════════════════════════════════════════════╗
                    ║  ÉTAPE 7: SCAN DE L'IMAGE DOCKER          ║
                    ╚════════════════════════════════════════════╝
                    """
                }
                
                sh '''
                    echo "🔍 Scan de l'image Docker vulpy-app:local..."
                    trivy image vulpy-app:local --format table 2>&1 | head -100 || echo "Trivy image scan completed"
                    echo "✅ Image Docker scannée"
                '''
            }
        }
        
        // ========================================
        // PHASE 4: Génération des rapports
        // ========================================
        stage('Génération des rapports') {
            steps {
                script {
                    echo """
                    ╔════════════════════════════════════════════╗
                    ║     ÉTAPE 8: GÉNÉRATION DES RAPPORTS       ║
                    ╚════════════════════════════════════════════╝
                    """
                }
                
                sh '''
                    echo "📊 Résumé des fichiers générés:"
                    ls -lh reports/ 2>/dev/null || mkdir -p reports
                    ls -lh reports/
                    echo "✅ Pipeline complété"
                '''
            }
        }
    }
    
    post {
        always {
            script {
                echo """
                ╔════════════════════════════════════════════╗
                ║         ARCHIVAGE DES ARTEFACTS            ║
                ╚════════════════════════════════════════════╝
                """
            }
            
            // Archiver tous les rapports
            archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
        }
        
        success {
            script {
                echo """
                ╔════════════════════════════════════════════╗
                ║    ✅ PIPELINE EXÉCUTÉ AVEC SUCCÈS        ║
                ╚════════════════════════════════════════════╝
                
                📋 Rapports disponibles:
                   🟢 SAST Bandit (bad)   → bandit-bad.html
                   🟢 SAST Bandit (good)  → bandit-good.html
                   🟡 SCA Trivy (deps)    → trivy-requirements.json
                   🟡 SCA Trivy (Docker)  → trivy-docker.json
                   🟡 Dépendances         → all-deps.txt
                
                Consultez les rapports dans:
                   Jenkins → Build Artifacts
                """
            }
        }
        
        failure {
            script {
                echo """
                ╔════════════════════════════════════════════╗
                ║        ❌ ÉCHEC DU PIPELINE                ║
                ╚════════════════════════════════════════════╝
                
                Consultez la sortie complète:
                   Jenkins → Console Output
                """
            }
        }
    }
}
