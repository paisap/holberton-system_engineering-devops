# configuration file with Puppet
file_line { 'Turn off':
  path => '/etc/ssh/ssh_config',
  line => ' PasswordAuthentication no'
}

file_line { 'Declare IdentityFile':
  path => '/etc/ssh/ssh_config',
  line => ' IdentityFile ~/.ssh/holberton'
}