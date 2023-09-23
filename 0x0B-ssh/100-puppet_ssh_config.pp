# creates an SSH configuration file so that you can connect to a server without typing a password.
file { 'config' :
    ensure  => file,
    path    => '/etc/ssh/ssh_config',
    content => 'HOST *
    HostName 18.206.208.78
    IdentityFile ~/.ssh/school
    User ubuntu
    PasswordAuthentication no
'
}
