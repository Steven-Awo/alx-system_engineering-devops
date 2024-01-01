#!/usr/bin/env bash
# Using puppet to configure file

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "# SSH client configuration
  Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
  ",
}
