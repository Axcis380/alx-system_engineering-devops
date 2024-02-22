# Increases the amount of traffic an Nginx server can handle.

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
#modify the ultimate file
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
# specify the path for sed cmd 
 path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx
exec { 'nginx-restart':
# restart nginx serv 
 command => '/etc/init.d/nginx restart',
# Specify the path for init.d scp
  path    => '/etc/init.d/'
}
