pipeline {
    agent any
  environment {
    VENV = 'venv'
}
    stages {
        stage('Clone repository') {
            steps {
                git branch: 'master',
                  url: 'https://github.com/lerod24/Projet_Git.git', credentialsId:'871ffda8-7f44-4339-a6b0-20a5ac2f7945'
            }
        }
        stage('setup python environment') {
            steps {
              bat '''
              python -m venv %VENV%
              call %VENV%\\Scripts\\activate
              pip install pytest
              '''
            }
        }
        stage('Run test with pytest') {
            steps {
                bat '''
                call %VENV%\\Scripts\\activate
                pytest --junitxml=report.xml
                '''
            
            }
        }
        stage('Deploy') {
            steps {
                echo 'Mise en production'
            }
        }
    }
    
    post {
        always{
            //publier resultats de test
            junit 'report.xml'
        }
        cleanup{
            //nettoyer l'environnement
            bat 'rmdir /s /q %VENV%'
            
        }
    }
    
}

