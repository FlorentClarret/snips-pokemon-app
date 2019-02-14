#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from application.intents.factory.Intent import Intent
from application.intents.impl.PokemonIdIntent import PokemonIdIntent
from application.intents.impl.PokemonNameIntent import PokemonNameIntent


class IntentFactory(object):

    @staticmethod
    def build(intent, config):
        if intent == Intent.POKEMON_ID:
            return PokemonIdIntent(config)
        if intent == Intent.POKEMON_NAME:
            return PokemonNameIntent(config)

        raise ValueError("No intent found for {}".format(intent))
