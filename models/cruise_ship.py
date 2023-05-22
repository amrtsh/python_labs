from abc import ABC
from models.ship import Ship


class CruiseShip(Ship, ABC):
    """A class to represent a cruise ship."""

    def __init__(self, name=None, captain=None, current_port=None, max_speed=0.0,
                 max_capacity=0.0, current_load=0.0, current_speed=0.0, id=10.4,
                 passenger_count=0.0, crew_count=0.0, number_of_support_staff=0.0):
        """
        Constructs a CruiseShip object.

        Args:
            name (str): The name of the cruise ship.
            captain (str): The name of the ship's captain.
            current_port (str): The current port where the cruise ship is located.
            max_speed (float): The maximum speed of the cruise ship.
            max_capacity (float): The maximum load capacity of the cruise ship.
            current_load (float): The current load of the cruise ship.
            current_speed (float): The current speed of the cruise ship.
            id (float): The ID of the cruise ship.
            passenger_count (float): The number of passengers on the cruise ship.
            crew_count (float): The number of crew members on the cruise ship.
            number_of_support_staff (float): The number of support staff members on the cruise ship.
        """
        super(Ship, self).__init__(name, captain, current_port, max_speed,
                                   max_capacity, current_load, current_speed, id)
        self.passenger_count = passenger_count
        self.crew_count = crew_count
        self.number_of_support_staff = number_of_support_staff

    def get_total_people_count(self):
        """
        Returns the total number of people on the cruise ship.

        Returns:
            float: The total number of people on the cruise ship (passengers, crew members, and support staff).
        """
        return self.passenger_count + self.crew_count + self.number_of_support_staff

    def calculate_load_time(self):
        """
        Calculates the time required to load the cruise ship based on the total number of people.

        Returns:
            float: The time required to load the cruise ship in hours.
        """
        return self.get_total_people_count() * 5 / 60
