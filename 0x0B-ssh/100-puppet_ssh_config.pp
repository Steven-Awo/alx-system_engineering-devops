#!/usr/bin/env bash
#Using puppet to configure file

file { 'etc/ssh/ssh_config':
	ensure => present,

content =>"

	#SSH client conffiguration
	host*
	IdentifyFile ~/.ssh/school
	PasswordAuthentication no
}
