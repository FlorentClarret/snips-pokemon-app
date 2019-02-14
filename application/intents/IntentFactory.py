#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from application.intents.Intent import Intent
from application.intents.PokemonIdIntent import PokemonIdIntent
from application.intents.PokemonNameIntent import PokemonNameIntent


class IntentFactory(object):

    @staticmethod
    def build(intent, config):
        if intent == Intent.POKEMON_ID:
            return PokemonIdIntent(config)
        if intent == Intent.POKEMON_NAME:
            return PokemonNameIntent(config)

        raise ValueError("No intent found for {}".format(intent))
