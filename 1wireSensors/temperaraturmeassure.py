# ==================================================
# File: temperaturmeassure.py
# Version: 0.0.012
# Date: 16.05.2020
# Author: Peter Weibel
# © 2013 - 2020 by PeWeSt 8712 Staefa info@pewest.ch
# ==================================================
#
# "0008030fb666"

import sys
import time
from w1thermsensor import W1ThermSensor
from time import sleep
sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18S20, "0008030fb666")

# i = 1
# while i < 4:
#    print("Messung:", i, f"{sensor.id:12} {sensor.get_temperature():>4.3f}")
#   sleep(0.1)
#   i += 1


i = 1
# Schreiben von einzelnen Strings, mit Zeilenende
# d.write("Temperatur Büro Peter\n")
for i in range(1,60,1):
    # Zugriffsversuch
    try:
        d = open("/home/pi/projects/1wireSensors/Daten", "a")
    except:
        print("Dateizugriff nicht erfolgreich")
        sys.exit(0)
    lt = time.localtime()
    # Entpacken des Tupels, Datum und Uhrzeit
    jahr, monat, tag = lt[0:3]
    stunde, minute, sekunde = lt[3:6]
    d.write(f"{tag:02d}.{monat:02d}.{jahr:4d};  ")
    d.write(f"  {stunde:02d}:{minute:02d}:{sekunde:02d};   ")
    d.write(f"{sensor.get_temperature():5.2f}")
    d.write("\n")
    print("Messung:", i, f"{sensor.id:12} {sensor.get_temperature():>4.3f}")

    sleep(5)

# Schliessen der Datei
    d.close()

