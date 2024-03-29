import RPi.GPIO as GPIO
import time
import socketserver
# from urlparse import parse_qs
# from BaseHTTPServer import BaseHTTPRequestHandler
import http.server
# RGB support has ended indefinitely


red = 19
green = 26
# blue = 13


# test_leds


def quantize(number):
    return (number * 100 / 255)


def set_color(col):
    R_Val = (col & 0xFF0000) >> 16
    G_Val = (col & 0x00FF00) >> 8
    B_Val = (col & 0x0000FF)
    R_Val = _quantize(R_Val)
    G_Val = _quantize(G_Val)
    B_Val = _quantize(.75 * B_Val)
    RED.ChangeDutyCycle(R_Val)
    GREEN.ChangeDutyCycle(G_Val)
    # BLUE.ChangeDutyCycle(B_Val)


def deactivate():
    RED.ChangeDutyCycle(1)
    GREEN.ChangeDutyCycle(1)
    # BLUE.ChangeDutyCycle(1)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
# GPIO.setup(blue,GPIO.OUT)

Freq = 100

RED = GPIO.PWM(red, Freq)
GREEN = GPIO.PWM(green, Freq)
# BLUE = GPIO.PWM(blue, Freq)


def test_leds():
    print ("Green LED on")
    GPIO.output(26,GPIO.HIGH)
    time.sleep(1)
    print ("Green LED off")
    GPIO.output(26,GPIO.LOW)
   
    print ("Red LED on")
    GPIO.output(19,GPIO.HIGH)
    time.sleep(1)
    print ("Red LED off")
    GPIO.output(19,GPIO.LOW)


def recieve_request():
    print ("Request Received")


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # url = parse_sq(self.path)
        # print "url: " + url
        if self.path == '/red':
            print ("Green LED shutoff from web")
            GPIO.output(26,GPIO.LOW)
            print ("Red LED on")
            GPIO.output(19,GPIO.HIGH)
        if self.path == '/green':
            print ("Red LED shutoff from web")
            GPIO.output(19,GPIO.LOW)
            print ("Green LED on")
            GPIO.output(26,GPIO.HIGH)
               
        content = bytes("{reply: 'success'}", "UTF-8")    
        self.send_response(200)    
        self.send_header("Content-type", "application/json")
        self.send_header("Content-Length", len(content))
        self.end_headers()
        self.wfile.write(content)


socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(("", 8080), Handler)
httpd.serve_forever()

_deactivate()

GPIO.cleanup()
