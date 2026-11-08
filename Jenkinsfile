pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Show Project Files') {
            steps {
                sh '''
                    find . -maxdepth 3 -type f
                '''
            }
        }

        stage('Run Python Program') {
            steps {
                sh '''
                    python3 sample_code.py
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    python3 -m pytest -v tests
                '''
            }
        }

        stage('Check Code Style') {
            steps {
                sh '''
                    pycodestyle sample_code.py --max-line-length=100
                '''
            }
        }
    }
}