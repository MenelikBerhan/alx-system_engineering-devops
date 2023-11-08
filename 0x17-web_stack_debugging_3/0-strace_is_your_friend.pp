# fix a typo error in /var/www/html/wp-settings.php
exec { 'install sed':
  command  => 'apt install sed -y',
  provider => shell,
  path     => ['/usr/bin', '/usr/sbin',],
}->exec { 'change line in wp-settings.php':
  command  => "sed -i 's/require_once( ABSPATH . WPINC . \x27\/class-wp-locale.phpp\x27 );/require_once( ABSPATH . WPINC . \x27\/class-wp-locale.php\x27 );/' /var/www/html/wp-settings.php",
  provider => shell,
  path     => ['/bin', '/usr/bin', '/usr/sbin',],
}-> exec { 'restart apache':
command  => 'service apache2 restart',
provider => shell,
  path   => ['/bin', '/usr/bin', '/usr/sbin',],
}
