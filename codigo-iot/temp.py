import dht
import machine
from time import sleep

d = dht.DHT22(machine.Pin(18))

while True:
  d.measure()
  t = d.temperature()
  h = d.humidity()

  print(t)
  print(h)
  
  sleep(1.0)




