#!/usr/bin/env python
import math


class Drone(object):

    def __init__(self, startingLocation, maximumWeight, nItemTypes):
        self.location = startingLocation
        self.maximumWeight = maximumWeight
        self.cargo = nItemTypes*[0]
        self.finishedAt = 0

    def load(self, nItems, itemType, warehouse):
        """Moves the drone to a target warehouse and takes the required items
        and increments its finishedAt counter"""
        turnsMoving = self._move(warehouse.location)
        warehouse.items[itemType] -= nItems
        self.cargo[itemType] += nItems
        self.finishedAt += turnsMoving + 1

    def deliver(self, nItems, itemType, customer):
        """Moves the drone to a target customer and drops the required items
        and increments its finishedAt counter"""
        turnsMoving = self._move(customer.location)
        self.cargo[itemType] -= nItems
        self.finishedAt += turnsMoving + 1

    def wait(self, nTurns):
        """Increments the finishedAt counter"""
        self.finishedAt += nTurns

    def _move(self, targetLocation):
        """Moves the drone to the targetLocation and returns the turns taken"""
        distance = math.sqrt(
            (self.location[0] - targetLocation[0])**2 +
            self.location[1] - targetLocation[1])
        self.location = targetLocation
        return math.ceil(distance)
