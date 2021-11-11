# Room_Booking_Device_Client
This is what must physically be installed on the device and run with cron.

Python 2 version: web_LED_py2\
Python 3 version: web_LED_py3

Add to crontab: 
sudo vi crontab -e\
@reboot python /path to script/wled.py

Add to LXDE:\
sudo vi ~/.config/lxsession/LXDE/autostart\
/usr/bin/chromium-browser --kiosk --disable-restore-session-state Location-of-Room_Booking_Web_Client

Remove mouse cursor: 
sudo apt-get install unclutter

add the following after install to ~/.config/lxsession/LXDE/autostart:\
@unclutter -idle 0.1\
/usr/bin/chromium-browser --kiosk --disable-restore-session-state [REPLACE THIS WITH SERVER SCRIPT URL]
