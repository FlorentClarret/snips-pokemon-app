#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from application.intents.Intent import Intent
from application.intents.PokemonIdIntent import PokemonIdIntent


class IntentFactory(object):

    @staticmethod
    def build(intent, config):
        if intent == Intent.POKEMON_ID:
            return PokemonIdIntent(config)

        raise ValueError("No intent found for {}".format(intent))
