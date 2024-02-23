# Install an especific version of werkzeug, flask (2.1.0)
#!/usr/bin/pup
package { 'werkzeug':
  ensure => '2.1.1',
  provider => 'pip3'
}

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
}
