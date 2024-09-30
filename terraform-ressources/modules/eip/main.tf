resource "aws_eip" "eip" {
    domain = "vpc"
    tags = {
        Name = "eip"
}
provisioner "local-exec" {
    command = "echo ${self.public_ip} > /var/jenkins_home/workspace/devops/instance_ip.txt"
}




} 
