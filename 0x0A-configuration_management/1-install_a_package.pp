#!/usr/bin/pup
# Install a specific version of flask (2.1.0)

exec { 'install_flask':
  command => 'pip3 install Flask==2.1.0',
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
}
