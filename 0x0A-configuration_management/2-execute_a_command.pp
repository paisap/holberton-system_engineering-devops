# Execute a proces
exec { 'pkill killmenow':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => 'pkill killmenow',
}
