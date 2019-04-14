#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum


class ConfigurationKey(Enum):
    MQTT = "mqtt"
    MQTT_ADDRESS = "address"
    MQTT_PORT = "port"

    POKEAPI = "pokeapi"
    POKEAPI_URL = "url"
