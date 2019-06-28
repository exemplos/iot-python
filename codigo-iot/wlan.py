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

print("ok")

name = "Francisco"
temp = 12.3
humid = 89

data = {"nome": name, "temp": temp, "humid": humid}
json = ujson.dumps(data)

headers = {'Content-Type': 'application/json'}
print(json)

while True:
  response = urequests.post("http://10.40.34.201:8080/temphumid/send", data=json, headers=headers)
  print("send")
  print(response.text)
  sleep(2.0)
# now use sockets as usual






