
from machine import Pin
import urequests
import network
import ujson
from time import sleep


def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Iot Smart House', 'IotSmartHousei8#!')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    
    
do_connect()

led = Pin(2, Pin.OUT)

print("ok")

led.value(1)
print("ligado")
sleep(1.0)
led.value(0)
print("desligado")


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








