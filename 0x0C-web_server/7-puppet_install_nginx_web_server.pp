# using puppet to automatically do the following

package { 'nginx':
  ensure => installed,

}

file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirecting_me https://www.github.com/Steven-Awo permanent;',

}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello world!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],

}
