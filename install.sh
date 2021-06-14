# Sys update and upgrade
apt-get update

# Install python and python tooling
# TODO: Check if python and pip is installed
apt-get install python3.6 python3-pip

# Python script dependencies
pip3 install RPi.GPIO smbus

# Enable i2c
# TODO: Write `i2c-bcm2708` and `i2c-dev` to `/etc/modules`

# Add cron startup
# TODO: Write `@startup /usr/bin/python3 /usr/share/poe/main.py &` to `crontab -e`
