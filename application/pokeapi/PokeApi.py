#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from application.config.ConfigurationKey import ConfigurationKey

POKE_API_DEFAULT_URL = "https://pokeapi.co/api/v2/"


class PokeApi:
    def __init__(self, config):
        self.config = config

    def get_pokemon(self, pokemon):
        base_url = self.config.get(ConfigurationKey.POKEAPI.value).get(ConfigurationKey.POKEAPI_URL.value,
                                                                       POKE_API_DEFAULT_URL)
        full_url = "{}pokemon/{}".format(base_url, pokemon)

        return requests.get(full_url).json()

    def get_pokemon_attribute(self, pokemon, pokemon_key):
        return str(self.get_pokemon(pokemon).get(pokemon_key.value))
