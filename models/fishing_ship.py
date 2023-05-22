from abc import ABC
from models.ship import Ship


class FishingShip(Ship, ABC):
    """A class to represent a fishing ship."""
    def __init__(self, name=None, captain=None, current_port=None, max_speed=0.0,
                 max_capacity=0.0, current_load=0.0, current_speed=0.0, id=10.4,
                 fisherman=0.0, crew_count=0.0):
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
        super(Ship, self).__init__(name, captain, current_port, max_speed,
                                   max_capacity, current_load, current_speed, id)
        self.current_load = current_load
        self.fisherman = fisherman
        self.crew_count = crew_count

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
