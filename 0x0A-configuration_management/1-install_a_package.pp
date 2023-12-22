#!/usr/bin/puppet

#To install flask of versio 2.1.0
package { 'flask':
  ensure  => '2.1.0',
  provider => 'pip3',
}
