#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from application.intents import PokemonIntent

POKEAPI_DEFAULT_URL = "https://pokeapi.co/api/v2/"


class SimplePokemonIntent(PokemonIntent.PokemonIntent):

    def __init__(self, config, message, key_name):
        super().__init__(config)
        self.message = message
        self.key_name = key_name

    def execute(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        pokemon = intent_message.slots.pokemon.first().value
        value = str(
            requests.get(
                "{}pokemon/{}".format(self.config.get("pokeapi").get("url", POKEAPI_DEFAULT_URL), pokemon)).json().get(
                self.key_name))

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, self.message.format(value),
                                                  "Pokemon App")
