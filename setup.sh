#!/bin/bash
apt-get update
apt-get upgrade
apt-get install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools nginx python3-venv

## Local server directory
mkdir /home/pi/locker_server
cd /home/pi/locker_server

python3 -m venv venv

source /home/pi/locker_server/venv/bin/activate

pip install -r requirements.txt


cp controller_lockers.service /etc/systemd/system/

systemctl start controller_lockers

systemctl enable controller_lockers

systemctl status controller_lockers

mv controller_lockers.nginx.conf /etc/nginx/sites-available/controller_lockers
ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled

nginx -t


systemctl restart nginx