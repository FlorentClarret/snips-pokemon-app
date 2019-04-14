#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes

from application.IntentCaller import IntentCaller
from application.config.ConfigurationKey import ConfigurationKey
from application.config.ConfigurationTools import SnipsConfigParser
from application.pokeapi.PokeApi import PokeApi

CONFIG_INI_FILE = "config.ini"

MQTT_DEFAULT_ADDRESS = "localhost"
MQTT_DEFAULT_PORT = "1883"

if __name__ == "__main__":

    try:
        configuration = SnipsConfigParser.read_configuration_file(CONFIG_INI_FILE)
    except:
        configuration = None

    mqtt_address = "{}:{}".format(
        configuration.get(ConfigurationKey.MQTT.value).get(ConfigurationKey.MQTT_ADDRESS.value, MQTT_DEFAULT_ADDRESS),
        str(configuration.get(ConfigurationKey.MQTT.value).get(ConfigurationKey.MQTT_PORT.value)), MQTT_DEFAULT_PORT)

    with Hermes(mqtt_address) as hermes:
        hermes.subscribe_intents(IntentCaller(PokeApi(configuration)).master_intent_callback).start()
