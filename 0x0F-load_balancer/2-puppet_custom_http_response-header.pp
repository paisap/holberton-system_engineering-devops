#task 0 with puppet
exec { 'add_header':
  command  => 'sudo apt update && sudo apt -y install nginx && echo "Holberton School" >> /var/www/html/index.html && sudo sed -i "60i\ \tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf && sudo service nginx restart',
  provider => 'shell',
}