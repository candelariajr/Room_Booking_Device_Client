import RPi.GPIO as GPIO
import time
import SocketServer
# from urlparse import parse_qs
from BaseHTTPServer import BaseHTTPRequestHandler

# RGB support has ended indefinitely


red = 19
green = 26
# blue = 13


def quantize(number):
    return number * 100 / 255


def set_color(col):
    r_val = (col & 0xFF0000) >> 16
    g_val = (col & 0x00FF00) >> 8
    # b_val = (col & 0x0000FF)
    r_val = quantize(r_val)
    g_val = quantize(g_val)
    # b_Val = quantize(.75 * b_val)
    RED.ChangeDutyCycle(r_val)
    GREEN.ChangeDutyCycle(g_val)
    # BLUE.ChangeDutyCycle(B_Val)


def _deactivate():
    RED.ChangeDutyCycle(1)
    GREEN.ChangeDutyCycle(1)
    # BLUE.ChangeDutyCycle(1)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
# GPIO.setup(blue,GPIO.OUT)

Freq = 100

RED = GPIO.PWM(red, Freq)
GREEN = GPIO.PWM(green, Freq)
# BLUE = GPIO.PWM(blue, Freq)

print("Green LED on")
GPIO.output(26, GPIO.HIGH)
time.sleep(1)
print("Green LED off")
GPIO.output(26, GPIO.LOW)

print("Red LED on")
GPIO.output(19, GPIO.HIGH)
time.sleep(1)
print("Red LED off")
GPIO.output(19, GPIO.LOW)


# Test function that has been deprecated
# def receive_request():
# print("Request Received")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # url = parse_sq(self.path)
        # print "url: " + url
        if self.path == '/red':
            print("Green LED shutoff from web")
            GPIO.output(26, GPIO.LOW)
            print("Red LED on")
            GPIO.output(19, GPIO.HIGH)
        if self.path == '/green':
            print("Red LED shutoff from web")
            GPIO.output(19, GPIO.LOW)
            print("Green LED on")
            GPIO.output(26, GPIO.HIGH)
        self.send_response(200)


SocketServer.TCPServer.allow_reuse_address = True
httpd = SocketServer.TCPServer(("", 8080), Handler)
httpd.serve_forever()

_deactivate()

GPIO.cleanup()
