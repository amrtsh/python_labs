"""
This module defines the FishingShip class, a subclass of Ship.
"""
from models.ship import Ship  # pylint: disable=import-error


class FishingShip(Ship):
    """A class to represent a fishing ship."""
    ship_power = {25000}

    def __init__(self, name=None, captain=None, current_port=None, max_speed=0.0,
                 max_capacity=0.0, current_load=0.0, current_speed=0.0,
                 fisherman=0.0, crew_count=0.0, id=10.4):
        """
        Constructs a FishingShip object.

        Args:
            name (str): The name of the fishing ship.
            captain (str): The name of the ship's captain.
            current_port (str): The current port where the fishing ship is located.
            max_speed (float): The maximum speed of the fishing ship.
            max_capacity (float): The maximum load capacity of the fishing ship.
            current_load (float): The current load of the fishing ship.
            current_speed (float): The current speed of the fishing ship.
            id (float): The ID of the fishing ship.
            fisherman (float): The number of fishermen on the fishing ship.
            crew_count (float): The number of crew members on the fishing ship.
        """
        # pylint: disable=invalid-name
        # pylint: disable=too-many-arguments
        # pylint: disable=redefined-builtin
        super().__init__(name, captain, current_port, max_speed,
                         max_capacity, current_load, current_speed, id)
        self.fisherman = fisherman
        self.crew_count = crew_count

    def __str__(self):
        """
            Returns a string representation of the ship object for convenient display.

            Returns:
                str: A string representation of the ship.
            """
        return (f"Ship: id-{self.id}, name-{self.name}, captain-{self.captain}, "
                f"current port-{self.current_port}, max speed-{self.max_speed}, "
                f"max capacity-{self.max_capacity}, current load-{self.current_load},"
                f"current speed-{self.current_speed}, fisherman-{self.fisherman}, "
                f"crew count-{self.crew_count}"
                )

    def get_total_people_count(self):
        """
        Returns the total number of people on the fishing ship.

        Returns:
            float: The total number of people on the fishing ship (crew members and fishermen).
        """
        return self.crew_count + self.fisherman

    def calculate_load_time(self):
        """
        Calculates the time required to load the fishing ship based on the current load.

        Returns:
            float: The time required to load the fishing ship in minutes.
        """
        return self.current_load * 60 / 20
