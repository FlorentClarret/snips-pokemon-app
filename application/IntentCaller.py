#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from application.intents.Intent import Intent
from application.intents.IntentFactory import IntentFactory


class IntentCaller:
    def __init__(self, config):
        self.config = config

    def master_intent_callback(self, hermes, intent_message):
        print('[master_intent_callback] intent: {}'.format(intent_message.intent.intent_name))

        try:
            intent = IntentFactory.build(Intent.from_name(intent_message.intent.intent_name), self.config)
            intent.execute(hermes, intent_message)
        except ValueError:
            print('[master_intent_callback] unknown intent {}'.format(intent_message.intent.intent_name))
            hermes.publish_start_session_notification(intent_message.site_id, "I did not understand", "Pokemon App")
