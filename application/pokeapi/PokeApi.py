#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

POKE_API_DEFAULT_URL = "https://pokeapi.co/api/v2/"


class PokeApi:
    def __init__(self, config):
        self.config = config

    def get_pokemon(self, pokemon):
        base_url = self.config.get("pokeapi").get("url", POKE_API_DEFAULT_URL)
        full_url = "{}pokemon/{}".format(base_url, pokemon)

        return requests.get(full_url).json()
