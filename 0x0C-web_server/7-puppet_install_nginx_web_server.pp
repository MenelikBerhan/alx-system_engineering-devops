# install and setup an nginx server
exec {'install nginx':
  provider => 'shell',
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx ; sudo echo "Hello World!" > /var/www/html/index.html ; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start'
}
