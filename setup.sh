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


cp locker_server.service /etc/systemd/system/

systemctl start locker_server

systemctl enable locker_server

systemctl status locker_server

mv locker_server.nginx.conf /etc/nginx/sites-available/locker_server
ln -s /etc/nginx/sites-available/locker_server /etc/nginx/sites-enabled

nginx -t


systemctl restart nginx