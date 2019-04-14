#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from application.intents import PokemonIntent
from application.pokeapi.PokemonKey import PokemonKey


class SimplePokemonIntent(PokemonIntent.PokemonIntent):

    def __init__(self, poke_api):
        super().__init__(poke_api)

    def execute(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        pokemon = intent_message.slots.pokemon.first()
        key = intent_message.slots.key.first()

        if pokemon is None:
            hermes.publish_start_session_notification(intent_message.site_id,
                                                      "I did not understand the pokemon name",
                                                      "Pokemon App")
            return

        if key is None:
            hermes.publish_start_session_notification(intent_message.site_id,
                                                      "I did not understand the attribute name",
                                                      "Pokemon App")
            return

        value = str(self.poke_api.get_pokemon_attribute(pokemon.value, PokemonKey.from_name(key.value)))

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id,
                                                  "{}'s {} is {}".format(pokemon.value, key.value.replace('_', ' '),
                                                                         value),
                                                  "Pokemon App")
