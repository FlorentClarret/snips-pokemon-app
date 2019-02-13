#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes

from application.IntentCaller import IntentCaller
from application.config.SnipsTools import SnipsConfigParser

CONFIG_INI_FILE = "config.ini"

MQTT_DEFAULT_ADDRESS = "localhost"
MQTT_DEFAULT_PORT = "1883"

if __name__ == "__main__":

    try:
        config = SnipsConfigParser.read_configuration_file(CONFIG_INI_FILE)
    except:
        config = None

    mqtt_address = "{}:{}".format(config.get("mqtt").get("address", MQTT_DEFAULT_ADDRESS),
                                  str(config.get("mqtt").get("port")), MQTT_DEFAULT_PORT)

    with Hermes(mqtt_address) as h:
        h.subscribe_intents(IntentCaller(config).master_intent_callback).start()
