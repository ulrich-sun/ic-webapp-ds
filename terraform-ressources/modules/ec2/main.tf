resource "aws_instance" "name" {
  ami = var.ami
  instance_type = var.instance_type 
  vpc_security_group_ids = [ var.sg_id ]
  key_name = var.key_name
  #subnet_id = var.subnet_id 
  associate_public_ip_address = true
  ebs_block_device {
    device_name = "/dev/sdf"
    volume_size = 20
    volume_type = "gp2"
  }

  root_block_device {
    delete_on_termination = true
  }

  tags = {
    Name = var.vm_name
  }

#  provisioner "local-exec" {
#    command = "echo IP: ${self.public_ip} > /var/jenkins_home/workspace/devops/instance_ip.txt"
#  }
}
