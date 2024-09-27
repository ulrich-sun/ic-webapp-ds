variable "ami" {
}

variable "instance_type" {
  default = "t2.medium"
}

variable "sg_id" {
}
variable "key_name" {
  default = "sun"
}

variable "subnet_id" {
}

variable "vm_name"{
  default = "ds-vm"
}