pipeline {
    agent none 
    environment {
        IMAGE_NAME = "ic-webapp"
        TAG_IMAGE = "v2.0"
        DOCKERHUB_ID = "ulrichsteve"
        DOCKERHUB_PASSWORD = credentials('dockerhub_password') 
        HOST_IP = "44.200.110.4"
        APP_EXPOSED = "8080"
        CONTAINER_PORT = "8080"

    }
    stages {
        stage ('Build Docker Image'){
            agent any
            steps {
                script {
                    sh' docker build --no-cache -f ./Docker-ressources/Dockerfile -t ${DOCKERHUB_ID}/${IMAGE_NAME}:${TAG_IMAGE} ./Docker-ressources'
                }
            }
        }
        stage ('Run Container'){
            agent any 
            steps {
                script {
                    sh ''' 
                    docker ps -a | grep -i $IMAGE_NAME && docker rm -f ${IMAGE_NAME}
                    docker run --rm --name ${IMAGE_NAME} -d -p ${APP_EXPOSED}:${CONTAINER_PORT} ${DOCKERHUB_ID}/${IMAGE_NAME}:${TAG_IMAGE}
                    sleep 5
                    '''
                }
            }
        }
        stage ('Test Container'){
            agent any 
            steps {
                script {
                    sh '''
                     curl -I http://${HOST_IP}:${APP_EXPOSED} | grep -i "200"
                    '''
                }
            }
        }
        stage ('Delete Container'){
            agent any 
            steps {
                script {
                    sh '''
                    docker stop ${IMAGE_NAME}
                    '''
                }
            }
        }
    }
}
