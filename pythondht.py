#Importar la librería de adafruit para poder utilizar el sensor DHT11 o DHT22
#Si no se tiene instalada esta librería no se puede importar y por tanto no funciona el código
#Descargar la librería de adafruit con el siguiente comando desde la terminal
#sudo pip3 install Adafruit_DHT
#By: Cristian Garcia

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
