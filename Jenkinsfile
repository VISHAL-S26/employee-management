pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/VISHAL-S26/employee-management.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    pip3 install --break-system-packages --upgrade pip
                    pip3 install --break-system-packages -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Deploy / Run App') {
            steps {
                sh '''
                    nohup python3 app.py > app.log 2>&1 &
                    sleep 3
                    curl -f http://localhost:5000 || (echo "App failed to start" && exit 1)
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully. App is running on port 5000.'
        }
        failure {
            echo 'Pipeline failed. Check the logs above for details.'
        }
        always {
            sh 'pkill -f "python3 app.py" || true'
        }
    }
}
