terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }
}

resource "local_file" "example" {
  filename = "${path.module}/hello.txt"
  content  = "Managed by Terraform! v2"
}