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
                    pip install --break-system-packages --upgrade pip
                    pip install --break-system-packages -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Free Port 5000') {
            steps {
                sh '''
                    fuser -k 5000/tcp || true
                    pkill -f "python3 app.py" || true
                    sleep 1
                '''
            }
        }

        stage('Deploy / Run App') {
            steps {
                sh '''
                    nohup python3 app.py > app.log 2>&1 &
                    sleep 3
                    echo "----- app.log -----"
                    cat app.log || true
                    echo "--------------------"
                    curl -f http://localhost:5000 || (echo "App failed to start - see app.log above" && exit 1)
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
