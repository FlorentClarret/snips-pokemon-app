#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes

from sample.IntentCaller import IntentCaller
from sample.tools.SnipsTools import SnipsConfigParser

CONFIG_INI_FILE = "config.ini"

MQTT_DEFAULT_ADDRESS = "localhost"
MQTT_DEFAULT_PORT = "1883"

if __name__ == "__main__":

    try:
        config = SnipsConfigParser.read_configuration_file(CONFIG_INI_FILE)
    except:
        config = None

    mqtt_address = "{}:{}".format(config.get("mqtt.address", MQTT_DEFAULT_ADDRESS),
                                  str(config.get("mqtt.port", MQTT_DEFAULT_PORT)))

    with Hermes(mqtt_address) as h:
        h.subscribe_intents(IntentCaller(config).master_intent_callback).start()
