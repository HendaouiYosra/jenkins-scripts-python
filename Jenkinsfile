pipeline {
  agent any
  environment {
        PATH = "/path/to/python/bin:${env.PATH}"
    }
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    
    stages {
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
