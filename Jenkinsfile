pipeline {
    agent {
        label "docker-agent"
    }
    stages {
        stage ("build") {
            steps {
                sh '''
                    docker build -t getpairs getpairs
                    docker build -t towords towords
                    docker build -t web web
                    docker network create build
                    '''
            }
        }
        stage ("deploy redis") {
            steps {
                sh 'docker run --network build -d -p 6379:6379 redis'
            }
        }
        stage ("get books urls") {
            steps {
                sh 'sh getbook.sh'
            }
        }
        stage ("to words!") {
            steps {
                sh 'docker run --name towords --network build towords $(cat url.txt)'
            }
        }
    }
    post {
        always {
            sh 'docker rm -f $(docker ps -aq) || true'
            sh 'docker image rm getpairs towords web'
            sh 'docker network rm build'
        }
    }
}