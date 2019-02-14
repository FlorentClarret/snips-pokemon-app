#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from application.intents.impl.SimplePokemonIntent import SimplePokemonIntent
from application.intents.factory.Intent import Intent


class IntentFactory(object):

    @staticmethod
    def build(intent, config):
        if intent == Intent.SIMPLE_QUERY:
            return SimplePokemonIntent(config)

        raise ValueError("No intent found for {}".format(intent))
