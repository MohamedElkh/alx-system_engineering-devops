# command to fix the problem of high amount or requests

exec { 'fix--for-nginx':
  provider => shell,
  command  => 'sed -i "s/15/4096/" /etc/default/nginx',
  path     => '/usr/local/bin/:/bin/'
}

exec { 'nginx-restart':
  provider => shell,
  command  => 'nginx restart',
  path     => '/etc/init.d/'
}
