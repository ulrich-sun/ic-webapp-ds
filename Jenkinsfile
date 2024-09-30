pipeline {
    agent none 
    environment {
        IMAGE_NAME = "ic-webapp"
        TAG_IMAGE = "v2.0"
        DOCKERHUB_ID = "ulrichsteve"
        DOCKERHUB_PASSWORD = credentials('dockerhub_password') 
        HOST_IP = 
        APP_EXPOSED = 8080
        CONTAINER_PORT = 8080

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
        stage ('push docker image'){
            agent any
            steps {
                script {
                    sh '''
                    echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_ID --password-stdin
                    docker push ${DOCKERHUB_ID}/${IMAGE_NAME}:${TAG_IMAGE}
                    '''
                }
            }
        }
        stage ('Build ec2 on aws using terraform'){
            agent {
                docker {
                    image 'jenkins/jnlp-agent-terraform'
                }
            }
            environment {
                AWS_ACCESS_KEY_ID = credentials('aws_access_key_id')
                AWS_SECRET_ACCESS_KEY = credentials('aws_secret_access_key')
                PRIVATE_AWS_KEY = credentials('private_aws_key')
            }
            steps {
                script {
                    sh '''
                    cd terraform-ressources/
                    terraform init
                    terraform apply -auto-approve
                    def instanceIP = sh (script: terraform output -raw instance_ip', returnStdout: true).trim()
                    echo " Voici ton adresse Ip: ${instanceIP}
                    '''
                }
            }
        }
        stage ('stage ansible'){
            agent {
                docker {
                    image 'registry.gitlab.com/robconnolly/docker-ansible:latest'
                }
            }
            steps {
                script {
                    def instanceIP = readFile('instance_ip.txt').trim()
                    sh '''
                    echo $PRIVATE_AWS_KEY > sun.pem
                    chmod 400 sun.pem
                    '''
                    write file: 'inventory.ini', test: "test-server\n${instanceIP} ansible_user=ubuntu ansible_ssh_private_key_file=sun.pem"
                    sh '''
                    cd ansible-ressources/
                    ANSIBLE_HOST_KEY_CHECKING=false ansible-playbook -i inventory.ini playbooks/install_docker.yaml
                    '''
                }
            }
        }
        stage ("delete ec2"){
            agent {
                docker {
                    image 'jenkins/jnlp-agent-terraform'
                }
            }
            environment {
                AWS_ACCESS_KEY_ID = credentials('aws_access_key_id')
                AWS_SECRET_ACCESS_KEY = credentials('aws_secret_access_key')
                PRIVATE_AWS_KEY = credentials('private_aws_key')
            }
            steps {
                script {
                    timeout(time: 30, unit: "MINUTES") {
                        input message: "Pour supprimer l'environnement appuis sur yes", ok: 'Yes'
                    }
                    sh '''
                    cd terraform-ressources/
                    terraform destroy -auto-approve
                    '''
                }
            }
        }

    }
}
