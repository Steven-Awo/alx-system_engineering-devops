#!/usr/bin/env puppet
# Installing tthe Ngiinx's package
package { 'nginx':
  ensure => installed,

}

file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => present,
  content => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],

}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/conf.d/custom_headers.conf'],

}
