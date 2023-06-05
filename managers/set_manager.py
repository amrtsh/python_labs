"""
SetManager Module
This module provides a SetManager class that allows iteration
and indexing over videos in a video manager.
Module Contents:
- SetManager: A class that provides iteration and indexing
functionality over videos in a video manager.
"""


class SetManager:
    """
       A class that manages a set of ship power values from a ship manager.

       The `SetManager` class provides iterable and indexing
       capabilities to access and manipulate ship power values.

       Args:
           ship_manager (ShipManager): The ship manager object.

       Attributes:
           ship_manager (ShipManager): The ship manager object.
           index (int): The current index for iteration.

       Methods:
           __iter__(): Returns an iterator over the ship power values.
           __len__(): Returns the total number of ship power values.
           __getitem__(index): Returns the ship power value at the specified index.
           __next__(): Returns the next ship power value.
    """

    def __init__(self, ship_manager):
        """
        Initialize the SetManager instance with a ShipManager object.
        ShipManager class containing the ships.
        """
        self.ship_manager = ship_manager
        self.index = 0

    def __iter__(self):
        """
        Return an iterator object that can iterate over the ships in the ship manager.
        """
        for ship in self.ship_manager:
            yield ship.ship_power

    def __len__(self):
        """
        Return the number of ships in the SetManager.
        """
        return sum(len(ship.ship_power) for ship in self.ship_manager)

    # reduce(sum(len(_obj)), self.ship_manager)
    def __getitem__(self, index):
        """
        Get the ship power value at the specified index.
        """
        if index >= len(self.ship_manager):
            raise IndexError("Index out of range")

        else:
            self.ship_manager[index]

    def __next__(self):
        """
        Get the next ship power value.
        """
        for ship in self.ship_manager:
            for power in ship.ship_power:
                yield power
