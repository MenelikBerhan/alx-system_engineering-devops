# remove file limit set in /etc/security/limits.conf for holberton user
exec {'remove config file and create empty one':
  command  => 'rm /etc/security/limits.conf && touch /etc/security/limits.conf',
  provider => shell,
  path     => ['/bin', '/usr/bin', '/usr/sbin',]
}
