# Collab As-Code Learning Project

Scripts and configs built while learning Git, Python, Ansible, and Terraform
for Cisco Collaboration automation.

## Setup
1. Copy `.env.example` to `.env` and add your Webex API token.
2. `pip3 install -r requirements.txt`

## Scripts
- `workspace_report.py` — exports all Webex workspaces to CSV
- `list_workspaces.yml` — Ansible equivalent
- `terraform-webex/` — Terraform data source reading workspaces