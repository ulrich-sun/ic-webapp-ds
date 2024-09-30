pipeline {
    agent none 
    stages {
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
                    '''
                    def instanceIP = sh(script: 'cat instance_ip.txt', returnStdout: true).trim()
                    echo "Voici ton adresse IP: ${instanceIP}"
                    writeFile file: 'instance_ip.txt', text: instanceIP
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
                    echo $PRIVATE_AWS_KEY > simple-stack.pem
                    chmod 400 simple-stack.pem
                    '''
                    writeFile file: 'inventory.ini', text: "test-server\n${instanceIP} ansible_user=ubuntu ansible_ssh_private_key_file=simple-stack.pem"
                    sh '''
                    cd ansible-ressources/playbooks/
                    ls -l
                    '''

                    sh '''
                    cd ansible-ressources/
                    ANSIBLE_HOST_KEY_CHECKING=false ansible-playbook -i inventory.ini ansible-ressources/playbooks/install-docker.yaml
                    '''
                }
            }
        }
        // Other stages...
    }
}
