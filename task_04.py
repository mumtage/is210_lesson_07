#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Buckingham Nicks"""

import data

data.BANDS['Buckingham Nicks'] = {
    'Lindsey Buckingham': ['guitar', 'vocals'],
    'Stevie Nicks': ['vocals', 'tamborine'],
    }

data.BANDS['Fleetwood Mac'].update(data.BANDS['Buckingham Nicks'])
