variable "ami" {
}

variable "instance_type" {
  default = "t2.medium"
}

variable "sg_name" {
}
variable "key_name" {
  default = "sun.pem"
}

variable "subnet_id" {
}