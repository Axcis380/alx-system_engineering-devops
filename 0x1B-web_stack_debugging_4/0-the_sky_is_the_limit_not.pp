# Increases the amount of traffic an Nginx server can handle.

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
#modify the ultimate value 
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
# specify the path for the sed command 
 path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx
exec { 'nginx-restart':
# restart nginx service 
 command => '/etc/init.d/nginx restart',
# Specify the path for the init.d script
  path    => '/etc/init.d/'
}
