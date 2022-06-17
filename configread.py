import configparser

config= configparser.ConfigParser()
config.read("config.ini")


relays= {}

for section in config.sections():
    relays[section] = {}
    for option in config.options(section):
        relays[section][option] = config.get(section, option)

print (relays)