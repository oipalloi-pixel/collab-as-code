terraform {
  required_providers {
    webex = {
      source  = "Nathan-Loisel/webex"
      version = ">= 0.1"
    }
  }
}

provider "webex" {
  # token pulled from WEBEX_ACCESS_TOKEN environment variable
}

data "webex_workspaces" "all" {}

output "workspace_names" {
  value = [for w in data.webex_workspaces.all.workspaces : w.display_name]
}