from pickle import TRUE
from Relay import Relay
import RPi.GPIO as GPIO
from time import sleep 
from datetime import datetime 
import os
from daemonize import Daemonize
import logging 
import configparser


# relays config 
config= configparser.ConfigParser()
config.read("config.ini")
relays= {}
for section in config.sections():
    relays[section] = {}
    for option in config.options(section):
        relays[section][option] = config.get(section, option)


pid = "/tmp/test.pid"
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False
fh = logging.FileHandler("/tmp/test.log", "w")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
keep_fds = [fh.stream.fileno()]


# configure relays


now =datetime.now()
weekday = now.weekday()
# 0 - monday ; 6 - Sunday
print(config.get("RELAY2","Pin"))
print(config.get("RELAY1","Pin"))


relay1=Relay( int(config.get("RELAY1","Pin")) )
relay2=Relay( int(config.get("RELAY2","Pin")) )

print(config.get("RELAY1","Pin"))
print (relay1.pin)
print(config.get("RELAY2","Pin"))
print (relay2.pin)

watering_hours =  int(config.get("DEFAULT","WateringHour"))
print (watering_hours)


def StartCycle():
    try:
        while TRUE:
            current_time= datetime.now().hour
            if watering_hours == current_time: 
                print ("entrou no primeiro\n")
                #start relays
                relay1.start()
                relay2.start()
            else: 
                relay1.stop()
                relay2.stop()
                print("stopped the relays")
            sleep(5) #pause for 10 minutes
            print ("entrou no cicl0") 
    except KeyboardInterrupt: 
        print('entered exception')
        GPIO.cleanup()
        os._exit(os.EX_OK)



daemon = Daemonize(app="RELAY", pid=pid, action=StartCycle, keep_fds=keep_fds)
daemon.start()
