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
                    sleep 2
                '''
            }
        }

        stage('Deploy / Run App') {
            steps {
                sh '''
                    nohup python3 app.py > app.log 2>&1 < /dev/null &
                    sleep 5

                    echo "----- app.log -----"
                    cat app.log || true
                    echo "--------------------"

                    curl -f http://127.0.0.1:5000
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully. Flask application is running on port 5000.'
        }

        failure {
            echo 'Pipeline failed. Check the logs above.'
        }

        always {
            echo 'Pipeline finished.'
        }
    }
}