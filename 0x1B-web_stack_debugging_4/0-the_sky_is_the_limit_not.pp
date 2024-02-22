# Fixes an nginx site that can't handle multiple concurrent requests
# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':

#modify the ultimate value
  command => "bash -c \"sed -iE 's/^ULIMIT=.*/ULIMIT=\\\"-n 8192\\\"/' \
/etc/default/nginx; service nginx restart\"",

# specify the path for the sed command
  path    => '/usr/bin:/usr/sbin:/bin'
}
