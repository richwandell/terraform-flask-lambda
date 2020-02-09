variable "aws_region" {
  description = "AWS Region"
  default = "us-east-1"
}

variable "backend_s3_bucket" {
  description = "Bucket for s3 backend"
  default = "terraform-state"
}

variable "runtime" {
  description = "Python version"
  default = "python3.6"
}