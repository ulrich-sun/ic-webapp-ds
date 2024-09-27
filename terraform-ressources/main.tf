provider "aws" {
  region = "us-east-1"
}

data "aws_vpc" "ds-vpc" {
  id = "vpc-0d69c6e9db73ad4d0"
}

data "aws_subnet" "ds-subnet" {
  id = "subnet-025fc5c8806c61117"
}

data "aws_security_group" "ds-sg" {
  id = "sg-0b5b395f56fad1e13"
}

#module "vpc" {
#  source = "./modules/vpc"
#}

#module "sg" {
#  source = "./modules/sg"
#  sg_name = "ds-sg"
#  vpc_id = data.aws_vpc.ds-vpc.id
#}

module "ec2" {
  source = "./modules/ec2"
  ami = "ami-0e86e20dae9224db8"
  instance_type = "t2.medium"
  sg_id = data.aws_security_group.ds-sg.id
  key_name = "sun"
  vm_name = var.vm_name
  subnet_id = data.aws_subnet.ds-subnet.id
}

module "eip" {
  source = "./modules/eip"
}

resource "aws_eip_association" "eip_assoc" {
    instance_id = module.ec2.ec2_id
    allocation_id = module.eip.eip_id
}