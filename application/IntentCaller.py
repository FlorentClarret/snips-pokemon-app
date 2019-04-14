#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from application.intents.factory.Intent import Intent
from application.intents.factory.IntentFactory import IntentFactory


class IntentCaller:
    def __init__(self, poke_api):
        self.poke_api = poke_api

    def master_intent_callback(self, hermes, intent_message):
        print('[IntentCaller] intent: {}'.format(intent_message.intent.intent_name))

        try:
            intent = IntentFactory.build(Intent.from_name(intent_message.intent.intent_name), self.poke_api)
            intent.execute(hermes, intent_message)
        except ValueError:
            print('[IntentCaller] unknown intent {}'.format(intent_message.intent.intent_name))
            hermes.publish_start_session_notification(intent_message.site_id, "I did not understand", "Pokemon App")
