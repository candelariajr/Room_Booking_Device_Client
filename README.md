# Room_Booking_Device_Client
This is what must physically be installed on the device and run with cron.

Python 2 version: web_LED_py2\
Python 3 version: web_LED_py3

If there is no lxsession directory:\
cp -r /etc/xdg/lxsession ~/.config/

Add to LXDE:\
sudo vi ~/.config/lxsession/LXDE-pi/autostart

python /path to script/wled.py\
@unclutter -idle 0.1\
/usr/bin/chromium-browser --kiosk --disable-pinch --disable-restore-session-state [REPLACE THIS WITH SERVER SCRIPT URL]
