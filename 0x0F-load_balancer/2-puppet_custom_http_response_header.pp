# install and setup an nginx server
exec {'install_nginx':
  provider => 'shell',
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx ; sudo service nginx start ;'
}

file_line { 'header':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  line    => "add_header X-Served-By \${hostname};",
  require => Exec['install_nginx']
}

exec {'restart_nginx':
  provider => 'shell',
  command  => 'sudo service nginx restart ;',
  require  => File_line['header']
}
