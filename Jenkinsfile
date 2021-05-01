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
                sh 'docker run --name redis --network build -d redis'
            }
        }
        stage ("to words!") {
            steps {
                sh 'docker run --name towords -i --network build towords'
                sh 'docker run --network build -i --rm redis redis-cli -h redis keys \'*\''
            }
        }
        stage ("get files!") {
            steps {
                sh 'docker run --name getpairs -i --network build -v $PWD/src:/app/src getpairs'
            }
        }
        stage ("start web!") {
            steps {
                sh 'docker run --name web -d --network build -v $PWD/src:/app/src web'
                sh 'docker run --rm -i --network build alpine apk add curl; curl localhost:3000/words'
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