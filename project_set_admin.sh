#!/bin/bash
license_plate=$(cat <(LC_ALL=C tr -dc a-z </dev/urandom | head -c 1) <(LC_ALL=C tr -dc a-z0-9 </dev/urandom | head -c 5) <(echo))
mkdir -p projects/$license_plate/accounts
touch projects/$license_plate/accounts/terragrunt.hcl
echo "this is a line" > projects/$license_plate/accounts/terragrunt.hcl
echo "project set created"