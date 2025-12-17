pipeline {
    agent any

    environment {
        IMAGE_NAME = "login-app"
        CONTAINER_NAME = "login-app-container"
        PORT = "5000"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Samhitha1705/flask-login-dashboard.git'
            }
        }

        stage('Docker Build') {
            steps {
                bat """
                docker build -t %IMAGE_NAME% .
                """
            }
        }

        stage('Docker Stop & Remove Existing Container') {
            steps {
                bat """
                docker stop %CONTAINER_NAME% || exit 0
                docker rm %CONTAINER_NAME% || exit 0
                """
            }
        }

        stage('Docker Run') {
            steps {
                bat """
                docker run -d -p %PORT%:%PORT% --name %CONTAINER_NAME% %IMAGE_NAME%
                """
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully! App should be running at http://localhost:%PORT%"
        }
        failure {
            echo "Pipeline failed. Check the console output for errors."
        }
    }
}
