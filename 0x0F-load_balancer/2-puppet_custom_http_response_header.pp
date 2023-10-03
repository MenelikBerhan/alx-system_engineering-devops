# install and setup an nginx server
exec {'install':
  provider => 'shell',
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx ; sudo echo "Hello World!" > /var/www/html/index.html ; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start'
}

file_line { 'header':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => ':80 default_server;',
  line    => "add_header X-Served-By ${hostname};",
  require => Exec['install']
}

service { 'nginx':
  ensure  => running,
  require => File_line['header']
}
