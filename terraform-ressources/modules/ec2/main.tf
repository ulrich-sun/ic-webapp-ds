resource "aws_instance" "name" {
  ami = var.ami
  instance_type = var.instance_type 
  security_groups = [ var.sg_name ]
  key_name = var.key_name
  subnet_id = var.subnet_id 

  ebs_block_device {
    device_name = "/dev/sdf"
    volume_size = 10
    volume_type = "gp2"
  }

  root_block_device {
    delete_on_termination = true
  }

  tags = {
    Name = "ds-vm"
  }
}
