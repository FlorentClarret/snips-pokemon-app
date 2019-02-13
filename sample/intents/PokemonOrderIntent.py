#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from sample.intents import PokemonIntent


class PokemonOrderIntent(PokemonIntent.PokemonIntent):

    def execute(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        pokemon = intent_message.slots.pokemon.first().value
        pokemon_order = str(
            requests.get("{}pokemon/{}".format(self.config.get("pokeapi").get("url"), pokemon)).json().get("order"))

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id,
                                                  "The " + pokemon + "'s order is " + pokemon_order,
                                                  "Pokemon App")
