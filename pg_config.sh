apt-get -qqy update
apt-get -qqy install python-dev
apt-get -qqy install libpq-dev
apt-get -qqy install postgresql python-psycopg2
apt-get -qqy install python-flask python-sqlalchemy
apt-get -qqy install python-pip
apt-get -qqy install libxml2-dev
apt-get -qqy install libxslt1-dev
sudo pip install -r /vagrant/requirements/local.txt
su postgres -c 'createuser -dRS vagrant'
su vagrant -c 'createdb'
su vagrant -c 'createdb shop'
