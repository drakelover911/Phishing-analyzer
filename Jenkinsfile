pipeline {
    agent any

    stages {
        stage("Checkout"){
            steps{
                git "https://github.com/jjkusio/Phishing-analyzer"
            }
            }
            stage("Build Docker image"){
                steps{
                    sh "docker build -t jjkusio/phishing-analyzer ."
                }
            }
            stage("Push"){
                steps{
                    sh "docker push jjkusio/phishing-analyzer"
                }
            }
        }
    }
