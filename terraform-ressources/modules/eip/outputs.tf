output "eip_id" {
  value = aws_eip.eip.id
}

output "eip_ip" {
  value = aws_eip.eip.public_ip
}