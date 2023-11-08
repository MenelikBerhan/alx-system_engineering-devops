# fix a typo error in /var/www/html/wp-settings.php
$old_text = 'require_once( ABSPATH . WPINC . \x27\/class-wp-locale.phpp\x27 );'
$new_text = 'require_once( ABSPATH . WPINC . \x27\/class-wp-locale.php\x27 );'
exec { 'install sed':
  command  => 'apt install sed -y',
  provider => shell,
  path     => ['/usr/bin', '/usr/sbin',],
}->exec { 'change line in wp-settings.php':
  command  => "sed -i 's/${old_text}/${new_text}/' /var/www/html/wp-settings.php",
  provider => shell,
  path     => ['/bin', '/usr/bin', '/usr/sbin',],
}-> exec { 'restart apache':
command  => 'service apache2 restart',
provider => shell,
  path   => ['/bin', '/usr/bin', '/usr/sbin',],
}
