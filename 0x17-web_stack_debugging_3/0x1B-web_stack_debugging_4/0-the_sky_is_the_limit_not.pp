# remove a config file with open file limit for nginx and restart nginx
exec {'remove config file':
  command  => 'rm /etc/default/nginx;',
  provider => shell,
  path     => ['/bin', '/usr/bin', '/usr/sbin',]
} -> exec {'restart nginx':
  command  => 'service nginx restart',
  provider => shell,
  path     => ['/bin', '/usr/bin', '/usr/sbin',]
}
