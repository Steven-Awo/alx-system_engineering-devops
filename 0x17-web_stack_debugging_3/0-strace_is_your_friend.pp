# A puppet's manuscript thats to replace just a line in the particular
file thats on a server

$filee_to_be_edited = '/var/www/html/wp-settings.php'

#replacing the line that containing "phpp" with "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${filee_to_be_edited}",
  path    => ['/bin','/usr/bin']
}
