from machine import Pin
import urequests
import network
import ujson
from time import sleep

# enable station interface and connect to WiFi access point
nic = network.WLAN(network.STA_IF)
nic.active(True)
#nic.connect('Iot Smart House', 'IotSmartHousei8#!')
nic.connect('LIVE TIM_41F9_2G', '2pxtrvv3hd')

led = Pin(2, Pin.OUT)

print("ok")

name = "Francisco"
temp = 12.3
humid = 89

data = {"name": name, "temp": temp, "humid": humid}
json = ujson.dumps(data)

headers = {'Content-Type': 'application/json'}
print(json)

while True:
  response = urequests.post("http://192.168.25.54:8080/temphumid/send", data=json, headers=headers)
  print("send")
  print(response.text)
  
  response = urequests.get("http://192.168.25.54:8080/temphumid/verifica", data=json, headers=headers)
  print(response.text)
  if(response.text == "on"):
    led.value(1)
  else:
    led.value(0)
  sleep(2.0)
# now use sockets as usual





