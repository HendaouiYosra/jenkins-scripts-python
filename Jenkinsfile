pipeline {
    agent any
    
    environment {
        PATH = "/path/to/python/bin:${env.PATH}"  // Replace with actual Python path if necessary
    }

    stages {
        stage('version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 install_jenkins.py'
            }
        }

        stage('hello') {
            steps {
                sh 'python3 hello.py'
            }
        }
    }
}
