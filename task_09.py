#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 07, Task 09"""

import task_09_utility

DATA_FILES = [
    {'data': 'task_09_data/router_01.csv'},
    {'data': 'task_09_data/router_02.csv'},
    {'data': 'task_09_data/router_03.csv'},
    ]

def load_data(DATA_FILES):
    counter = 0
    loaded = {}
    for item in DATA_FILES:
        loaded[counter + 1] = task_09_utility.get_data(item['data']),
        counter += 1
    return loaded


def merge_data(dictionary):
    merged = {}
    for k, v in dictionary.iteritems():
        for a in v:
            for b in a:
                temp = dictionary[k][0][b - 1]['clock']
                merged.update(temp)
        return merged

x = load_data(DATA_FILES)
y = task_09_utility.get_data('task_09_data/router_01.csv')
