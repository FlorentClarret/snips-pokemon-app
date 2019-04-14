#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.ontology import *


class PokemonIntent(object):

    def __init__(self, poke_api):
        self.poke_api = poke_api

    def execute(self, hermes, intent_message):
        raise NotImplementedError("Should have implemented this")
