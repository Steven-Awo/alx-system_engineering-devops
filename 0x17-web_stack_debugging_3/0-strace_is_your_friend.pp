# A puppet's manuscript thats to replace just a line in the particular file thats on a server

$file_to_editt = '/var/www/html/wp-settings.php'

#replacing the line that containing "phpp" with "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_editt}",
  path    => ['/bin','/usr/bin']
}
