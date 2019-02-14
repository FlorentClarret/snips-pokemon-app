#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from application.intents.PokemonIdIntent import PokemonIdIntent


class IntentCaller:
    def __init__(self, config):
        self.config = config

    def master_intent_callback(self, hermes, intent_message):
        intent = None
        coming_intent = intent_message.intent.intent_name

        print('[master_intent_callback] intent: {}'.format(coming_intent))

        if coming_intent == 'florentclarret:PokemonId':
            intent = PokemonIdIntent(self.config)

        if intent is not None:
            intent.execute(hermes, intent_message)
        else:
            hermes.publish_start_session_notification(intent_message.site_id, "I did not understand", "Pokemon App")
