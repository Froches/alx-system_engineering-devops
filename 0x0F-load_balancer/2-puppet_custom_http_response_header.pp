# 2-puppet_custom_http_response_header.pp

node default {
  class { 'nginx': }

  nginx::resource::server { 'default':
    ensure       => present,
    listen_port  => 80,
    server_name  => ['localhost', $::fqdn],
    www_root     => '/var/www/html',
    index_files  => ['index.html'],
    autoindex    => 'off',
    headers      => { 'X-Served-By' => $::hostname },
  }
}
