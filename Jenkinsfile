pipeline {
    agent any

    // Force Jenkins to see the Mac system paths
    environment {
        PATH = "/opt/homebrew/bin:/usr/local/bin:$PATH"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose up -d'
            }
        }

        stage('Verify') {
            steps {
                // Pause execution to let the Flask container boot
                sh 'sleep 5'
                // Hit the local port to verify the application is alive
                sh 'curl -f http://localhost:5000/ || exit 1'
            }
        }
    }
}
