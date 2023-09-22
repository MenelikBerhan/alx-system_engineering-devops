# creates a file called school in /etc
file { 'school' :
    ensure  => file,
    path    => '/etc/school',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet'
}
