# command to fix the problem of high amount or requests

exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  befoe    => Exec['rest'],
}

exec {'rest':
  provider => shell,
  command  => 'sudo service nginx restart',
}
