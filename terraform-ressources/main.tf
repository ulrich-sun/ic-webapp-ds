provider "aws" {
  region = "us-east-1"
}

module "vpc" {
  source = "./modules/vpc"
}

module "sg" {
  source = "./modules/sg"
  sg_name = "ds-sg"
  vpc_id = module.vpc.vpc_id
}

module "ec2" {
  source = "./modules/ec2"
  ami = "ami-0e86e20dae9224db8"
  instance_type = "t2.medium"
  sg_id = module.sg.sg_id
  key_name = "sun"
  subnet_id = module.vpc.subnet_id
}

module "eip" {
  source = "./modules/eip"
}

resource "aws_eip_association" "eip_assoc" {
    instance_id = module.ec2.ec2_id
    allocation_id = module.eip.eip_id
}