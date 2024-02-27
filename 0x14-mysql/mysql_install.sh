#!/usr/bin/env bash
# Installing mysql on database
sudo apt update
sudo apt upgrade
sudo apt install mysql-server
sudo mysql_secure_installation
sudo systemctl status mysql
