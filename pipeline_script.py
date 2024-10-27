pipeline {
    agent any
    
    environment {
        PYTHON_HOME = 'C:\\Users\\soory\\AppData\\Local\\Programs\\Python\\Python313'
        PATH = "${PYTHON_HOME};${PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[credentialsId: 'f9032ac3-deb6-47ca-8665-119ec7c1cb11', url: 'https://github.com/Soorya-205/dev_pro.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', credentialsId: 'f9032ac3-deb6-47ca-8665-119ec7c1cb11', url: 'https://github.com/Soorya-205/dev_pro.git'
                bat 'python sort.py'
                
            }
        }
        stage('Test') {
            steps {
                echo "Testing is done"
            }
        }
    }
}
