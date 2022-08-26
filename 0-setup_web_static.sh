#!/usr/bin/env bash
# Update package
sudo apt update
# Install nginx
sudo apt install -y nginx
#create directory
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
#create a fake html file
sudo echo $'<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>' | sudo tee /data/web_static/releases/test/index.html
#create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
#Give ownership
sudo chown -hR ubuntu:ubuntu /data/
#configuration to serve the content
#Cheker no paso con sed
#new_string="a location /hbnb_static/\n\t{\n\t\talias /data/web_static/current/;\n\t}"
#sudo sed -i "/server_name _;/$new_string" /etc/nginx/sites-available/default
echo "
server {
        listen 80 default_server;
        listen [::]:80 default_server;
        server_name _;
        add_header X-Served-By $HOSTNAME;
        root   /var/www/html;
        index  index.html index.htm;
        location /hbnb_static {
                alias /data/web_static/current;
                index index.html index.htm;
        }
}
" | sudo tee /etc/nginx/sites-available/default
#restart nginx
sudo service nginx restart
