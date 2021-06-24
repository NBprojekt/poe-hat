# PoE Hat
Setup of waveshare poe head b

![IMG_20210624_172216](https://user-images.githubusercontent.com/24683383/123290525-a5567880-d511-11eb-9e17-bfab224742c2.jpg)


## Install python and python tooling
```
apt-get update && apt-get install python3.6 python3-pip
```

## Installation library
```
pip3 install RPi.GPIO smbus
```

## Enable i2c module
Add the following modules to `/etc/modules`: 
- `i2c-bcm2708` 
- `i2c-dev` 

## Pull repo into 
```
git clone https://github.com/NBprojekt/poe-head.git /usr/share/poe-hat
```

## Add script to startup
Open crontab `crontab -e` and add the following line `@startup /usr/bin/python3 /usr/share/poe-hat/src/main.py &`
