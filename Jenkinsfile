pipeline {
    agent {
        label "docker-agent"
    }
    stages {
        stage ("test") {
            steps {
                sh 'ls'
                sh 'pwd'
                sh 'docker version'
            }
        }
    }
    post {
        always {
            sh 'docker rm -f $(docker ps -aq)'
        }
    }
}