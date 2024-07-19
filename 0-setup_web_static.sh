#!/usr/bin/env bash
# configure server to deploy web_static

sudo apt -y update
sudo apt -y upgrade
sudo apt -y install nginx

sudo mkdir -p /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
echo "Testing mic check 1,2,3" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
