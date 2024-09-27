resource "aws_eip" "eip" {
    domain = "vpc"
    tags = {
        Name = "eip"
    }
} 