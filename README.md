
- Install RPI Imager
  ```
  snap install rpi-imager
  ```
- Download Raspberry PI OS Lite

- In the settings of RPI Imager enable SSH & configure the WIFI settings


## Set up wifi & SSH on Pi Zero W (Legacy)

- Create `wpa_supplicant.conf` file to your boot directory. Assuming Raspian stretch:

```
country=UK # Your 2-digit country code
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
    ssid="YOUR_NETWORK_NAME"
    psk="YOUR_PASSWORD"
    key_mgmt=WPA-PSK
}
```
- Add file named `ssh` to root of boot directory
- Put the SD card in the Pi and start up

(See https://howchoo.com/g/ndy1zte2yjn/how-to-set-up-wifi-on-your-raspberry-pi-without-ethernet & https://desertbot.io/blog/headless-pi-zero-w-wifi-setup-windows)


## Connect to the PI

Once booted, search for the rapsberry pi

```
nmap -sP 192.168.0.0/24
```

SSH onto the pi using password authentication
```
ssh -o PreferredAuthentications=password pi@<pi-ip-address>
```

## Requirements

```
    sudo apt-get update
    sudo apt install pip
    sudo apt-get install libgles2-mesa-dev

    sudo pip3 install adafruit-circuitpython-motorkit
    sudo pip3 install ds4drv
    sudo pip3 install pygame
```

## Start DS4DRV (Dual Shock bluetooth) on start-up

Create systemd file for dsdrv.

```
sudo nano /etc/systemd/system/ds4drv.service
```

with the context

```
[Unit]
Description=DS4 Driver Service
After=bluetooth.target
Requires=bluetooth.target

[Service]
ExecStart=/usr/local/bin/ds4drv
Restart=always
User=root
# Wait a few seconds to let Bluetooth initialize
ExecStartPre=/bin/sleep 5
StandardOutput=syslog
StandardError=syslog

[Install]
WantedBy=multi-user.target
```
 
Then run

```
sudo systemctl daemon-reload
sudo systemctl enable ds4drv
sudo systemctl restart ds4drv
```

## Install script
    
```
scp -o PreferredAuthentications=password -r src pi@192.168.1.145:/home/pi/mark01-src
```


# Test run

SSH on to pi

```
ssh -o PreferredAuthentications=password pi@<pi-ip-address>
```

On the PS4 controller hold down share and PS4 button

Once connected, run the script on the pi:
  
```
sudo python3 controller_demoy.py
```




## Executing script on start-up

See https://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up
https://www.raspberrypi.org/forums/viewtopic.php?t=95101

## On/off button

https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi

## On/off status light



## Stepper
- https://www.waveshare.com/wiki/Stepper_Motor_HAT
- https://www.youtube.com/watch?v=8nMbXOeY1qs
- https://www.youtube.com/watch?v=0WQNXruPaqg
- https://www.youtube.com/watch?v=Omm6_QxtJ04
- https://www.waveshare.com/w/upload/b/b2/Stepper_Motor_HAT_User_Manual_EN.pdf

## Equipment

 - Raspberry Pi Zero W
 - [Stepper Motor HAT for Raspberry Pi](https://www.amazon.co.uk/gp/product/B07PXF5DZ7/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)
 - [perseids 2WD Robot Chassis](https://www.amazon.co.uk/gp/product/B07DNX1DX9/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)


# Wiring notes

- In Motor Hat wire LEFT wheel (black, red) into M4, and RIGHT wheel into M1 (red,black)
  so it should be RWred, RWblack, -, -, -, -,-,-, LWblack, LWRed
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  https://raspberrypi.stackexchange.com/questions/137164/ssh-into-raspberry-pi-os-lite-not-working
  
  
