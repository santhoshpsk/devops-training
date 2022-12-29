provider "aws" {
  region     = "ap-south-1"
  access_key = "AKIA53OQIJSG3TTURQEK"
  secret_key = "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"
}

resource "aws_instance" "ec2-instance-1" {
    ami = "ami-03d3eec31be6ef6f9"
    instance_type = "t2.micro"
    tags = {
      "name" = "instance1"
    }
    root_block_device {
        volume_size = 20
    }
}

output "AWS-Instance-public-ip" {
    value = aws_instance.ec2-instance-1.public_ip
}