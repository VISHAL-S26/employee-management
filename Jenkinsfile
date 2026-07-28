pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/VISHAL-S26/employee-management.git'
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    python3 -m py_compile app.py
                '''
            }
        }

        stage('Deploy / Run App') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
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
