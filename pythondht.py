import Adafruit_DHT
import time

sensor_dht = Adafruit_DHT.DHT11
pin_dht = 4

while True:
    humedad, temperatura = Adafruit_DHT.read(sensor_dht,pin_dht)
    if humedad is not None and temperatura is not None:
        print("T={0:0.1f}C H={1:0.1f}%".format(temperatura,humedad))
    else:
        print("Falla en la lectura")
    time.sleep(3)
