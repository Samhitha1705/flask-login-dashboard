pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Samhitha1705/flask-login-dashboard.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Code Validation') {
            steps {
                sh 'python -m py_compile app.py'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t flask-login-app .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker stop flask-login || true
                docker rm flask-login || true
                docker run -d -p 5000:5000 --name flask-login flask-login-app
                '''
            }
        }
    }
}
