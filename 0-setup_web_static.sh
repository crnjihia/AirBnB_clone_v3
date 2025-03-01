#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static.

# Install Nginx 
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create required directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/releases/test/index.html

# Create a emty HTML file
echo "<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

echo "server {
    listen 80;
    server_name localhost;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }
}" | sudo tee /etc/nginx/sites-available/default

# Restart
sudo service nginx restart
