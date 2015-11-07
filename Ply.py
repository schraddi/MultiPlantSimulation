#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Ply(object):
    def __init__(self, orientation, fiberAreaWeight, placingTime):
        self.orientation = orientation
        self.placingTime = placingTime
        self.fiberAreaWeight = fiberAreaWeight
        self.placed = False

    def __str__(self):
        output =    'Orientation: ' + str(self.orientation) + '°\n' + \
                    'Fiber Area Weight: ' + str(self.fiberAreaWeight) + ' g\m2\n' + \
                    'Placing Time: ' + str(self.placingTime) + ' s\n'
        if self.placed:
            output += 'Ply has been placed already.'
        else:
            output += 'Ply has not been placed so far.'

        return output
