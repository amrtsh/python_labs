from abc import ABC

from models.ship import Ship


class CargoShip(Ship, ABC):
    """A class to represent a cargo ship."""
    def __init__(self, id=10.4, name=None, captain=None, current_port=None, max_speed=0.0,
                 max_capacity=0.0, current_load=0.0, current_speed=0.0,
                 crew_count=0.0, tonnage=0.0, type_of_cargo=None):
        """
        Constructs a CargoShip object.

        Args:
            name (str): The name of the cargo ship.
            captain (str): The name of the ship's captain.
            current_port (str): The current port where the cargo ship is located.
            max_speed (float): The maximum speed of the cargo ship.
            max_capacity (float): The maximum load capacity of the cargo ship.
            current_load (float): The current load of the cargo ship.
            current_speed (float): The current speed of the cargo ship.
            id (float): The ID of the cargo ship.
            crew_count (float): The number of crew members on the cargo ship.
            tonnage (float): The tonnage of the cargo ship.
            type_of_cargo (str): The type of cargo carried by the cargo ship.
        """
        super(Ship, self).__init__(name, captain, current_port, max_speed,
                                   max_capacity, current_load, current_speed, id)
        self.current_load = current_load
        self.crew_count = crew_count
        self.tonnage = tonnage
        self.type_of_cargo = type_of_cargo

    def get_total_people_count(self):
        """
        Returns the total number of people on the cargo ship.

        Returns:
            float: The total number of people on the cargo ship (crew members).
        """
        return self.crew_count

    def calculate_load_time(self):
        """
        Calculates the time required to load the cargo on the cargo ship.

        Returns:
            float: The time required to load the cargo in minutes.
        """
        return self.current_load * 60 / 20
