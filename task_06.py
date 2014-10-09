#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 07, Task 05... er, 6"""


import data

SUPER_SIDEKICKS = {}
for HERO, HERO_DATA in data.SUPERHEROES.iteritems():
    SUPER_SIDEKICKS[HERO] = data.SUPERHEROES[HERO].get('pet')
