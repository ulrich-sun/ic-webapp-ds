resource "aws_vpc" "vpc" {

    cidr_block = "172.16.0.0/16"

    tags = {
        Name= "ds-vpc"
    }
}

resource "aws_subnet" "subnet" {

    vpc_id = aws_vpc.vpc.id
    cidr_block = "172.16.10.0/24"

    tags = {
        Name= "ds-subnet"
    }
} 

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.vpc.id 

  tags =  {
    Name = "ds-igw"
  }
}

resource "aws_route_table" "rt" {
  vpc_id = aws_vpc.vpc.id 
  route = { 
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
  tags = {
    Name = "rt"
  }
}

resource "aws_route_table_association" "rta" {
    subnet_id = aws_subnet.subnet.id
    route_table_id = aws_route_table.rt.id
    depends_on = [aws_subnet.subnet, aws_route_table.rt]
}
