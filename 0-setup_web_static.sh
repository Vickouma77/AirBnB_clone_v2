#!/usr/bin/env bash
#script that sets up your web servers for the deployment

#installing nginx if not exist
apt-get -y update
apt-get -y install nginx

#Creating static folders
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "<!DOCTYPE html>
      <html>
      <head>
      </head>
      <body>
         <p>deployment test for vickouma.tech</p>
      </body>
      </html>" | tee /data/web_static/releases/test/index.html

#creating a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

#change ownership
chown ubuntu:ubuntu /data

#configuring nginx
sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default

service nginx restart
