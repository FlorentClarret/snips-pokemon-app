#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from hermes_python.ontology import *


class PokemonIntent(object):

    def __init__(self, config):
        self.config = config

    def execute(self, hermes, intent_message):
        raise NotImplementedError("Should have implemented this")
