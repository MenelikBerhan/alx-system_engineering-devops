# install and setup an nginx server
exec {'install nginx':
  provider => 'shell',
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx ; sudo service nginx start'
}

file_line { 'header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => ':80 default_server;',
  line   => "add_header X-Served-By ${hostname};"
}

exec {'restart nginx':
  provider => 'shell',
  command  => 'sudo service nginx restart'
}
