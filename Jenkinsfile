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
                    # Créer venv si nécessaire
                    if [ ! -d "/var/jenkins_home/bandit-venv" ]; then
                        echo "📦 Création de l'environnement Bandit..."
                        python3 -m venv /var/jenkins_home/bandit-venv
                        . /var/jenkins_home/bandit-venv/bin/activate
                        pip install bandit==1.8.6
                    fi
                    
                    . /var/jenkins_home/bandit-venv/bin/activate
                    
                    cd /project
                    
                    echo "🔍 Analyse du code vulnérable (bad/)..."
                    
                    # Analyse détaillée en HTML
                    bandit -r bad -f html -o ${WORKSPACE}/reports/bandit-bad.html
                    
                    # Analyse en JSON pour traitement
                    bandit -r bad -f json -o ${WORKSPACE}/reports/bandit-bad.json
                    
                    # Affichage dans la console
                    echo ""
                    echo "📋 Résumé Bandit (bad/):"
                    bandit -r bad -f screen || true
                    
                    echo "✅ Rapport HTML: reports/bandit-bad.html"
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
                    
                    cd /project
                    
                    echo "🔍 Analyse du code corrigé (good/)..."
                    
                    bandit -r good -f html -o ${WORKSPACE}/reports/bandit-good.html
                    bandit -r good -f json -o ${WORKSPACE}/reports/bandit-good.json
                    
                    echo ""
                    echo "📋 Résumé Bandit (good/):"
                    bandit -r good -f screen || true
                    
                    echo "✅ Rapport HTML: reports/bandit-good.html"
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
                    echo "📊 Génération du rapport comparatif..."
                    
                    BAD_COUNT=\$(grep -o '"severity"' ${WORKSPACE}/reports/bandit-bad.json 2>/dev/null | wc -l || echo "0")
                    GOOD_COUNT=\$(grep -o '"severity"' ${WORKSPACE}/reports/bandit-good.json 2>/dev/null | wc -l || echo "0")
                    
                    echo ""
                    echo "┌─────────────────────────────────────────┐"
                    echo "│ RÉSULTATS SAST (Bandit)                 │"
                    echo "├─────────────────────────────────────────┤"
                    echo "│ Code VULNÉRABLE (bad/)  : $BAD_COUNT vulnérabilités"
                    echo "│ Code CORRIGÉ (good/)     : $GOOD_COUNT vulnérabilités"
                    echo "│ Amélioration              : $(($BAD_COUNT - $GOOD_COUNT)) vulnérabilités corrigées"
                    echo "└─────────────────────────────────────────┘"
                    echo ""
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
                    cd /project
                    
                    echo "📦 Scan du fichier requirements.txt..."
                    trivy fs --format json --output ${WORKSPACE}/reports/trivy-requirements.json requirements.txt
                    
                    echo ""
                    echo "🔍 Résultats du scan requirements.txt:"
                    trivy fs --format table requirements.txt || true
                    
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
                    cd /project
                    
                    echo "🔍 Analyse complète du répertoire (dépendances + secrets)..."
                    
                    # Scan complet
                    trivy fs --format json --output ${WORKSPACE}/reports/trivy-supply-chain.json .
                    
                    # Scan des secrets potentiels
                    trivy fs --scanners secret --format json --output ${WORKSPACE}/reports/trivy-secrets.json . || true
                    
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
                    cd /project
                    
                    echo "📊 Installation des dépendances pour analyse complète..."
                    
                    python3 -m venv /tmp/scan-venv
                    . /tmp/scan-venv/bin/activate
                    pip install --quiet -r requirements.txt
                    pip freeze > ${WORKSPACE}/reports/all-deps.txt
                    
                    echo "📋 Dépendances installed (transitives incluses):"
                    cat ${WORKSPACE}/reports/all-deps.txt
                    
                    echo ""
                    echo "🔍 Scan Trivy des dépendances transitives..."
                    trivy fs ${WORKSPACE}/reports/all-deps.txt || true
                    
                    echo "✅ Dépendances transitives analysées"
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
                    cd /project
                    
                    echo "🐳 Construction de l'image Docker: vulpy-app:local"
                    docker build -t vulpy-app:local .
                    
                    echo ""
                    docker images | grep vulpy-app
                    
                    echo "✅ Image Docker construite avec succès"
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
                    
                    # Scan en JSON
                    trivy image --format json --output ${WORKSPACE}/reports/trivy-docker.json vulpy-app:local
                    
                    # Affichage en table
                    echo ""
                    echo "📊 Résultats du scan Docker:"
                    trivy image --format table vulpy-app:local || true
                    
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
                    echo ""
                    ls -lh ${WORKSPACE}/reports/
                    
                    echo ""
                    echo "📈 Statistiques:"
                    echo "  - Rapports SAST: $(ls -1 ${WORKSPACE}/reports/bandit-*.html 2>/dev/null | wc -l)"
                    echo "  - Rapports JSON: $(ls -1 ${WORKSPACE}/reports/*.json 2>/dev/null | wc -l)"
                    echo "  - Fichiers texte: $(ls -1 ${WORKSPACE}/reports/*.txt 2>/dev/null | wc -l)"
                    
                    echo ""
                    echo "✅ Tous les rapports générés"
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
            
            // Publier les rapports HTML
            publishHTML([
                reportDir: 'reports',
                reportFiles: 'bandit-bad.html, bandit-good.html',
                reportName: '📊 Rapports SAST + SCA',
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true
            ])
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
