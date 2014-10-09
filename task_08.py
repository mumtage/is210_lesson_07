#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 07, Task 08"""

from data import FRUIT


def get_cost_per_item(shoplist):
    """get total cost of shoplist items based on shoplist quantities"""

    cost_per_item = {
        k: FRUIT[k]*q for k, q in shoplist.iteritems() if k in FRUIT
        }
    return cost_per_item


def get_total_cost(shoplist):
    """returns total cost of shoplist"""
    total_cost = sum(get_cost_per_item(shoplist).values())
    return total_cost
