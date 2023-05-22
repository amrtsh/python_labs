"""
This module defines the MilitaryShip class, a subclass of Ship.
"""
from models.ship import Ship  # pylint: disable=import-error


class MilitaryShip(Ship):
    """A class to represent a military ship."""

    def __init__(self, name=None, captain=None, current_port=None, max_speed=0.0,
                 max_capacity=0.0, current_load=0.0, current_speed=0.0, id=10.4,
                 military=0.0, crew_count=0.0):
        """
            Constructs a MilitaryShip object.

            Args:
                name (str): The name of the military ship.
                captain (str): The name of the ship's captain.
                current_port (str): The current port where the military ship is located.
                max_speed (float): The maximum speed of the military ship.
                max_capacity (float): The maximum load capacity of the military ship.
                current_load (float): The current load of the military ship.
                current_speed (float): The current speed of the military ship.
                id (float): The ID of the military ship.
                military (float): The number of military personnel on the military ship.
                crew_count (float): The number of crew members on the military ship.
        """
        # pylint: disable=invalid-name
        # pylint: disable=too-many-arguments
        # pylint: disable=redefined-builtin
        super().__init__(name, captain, current_port, max_speed,
                         max_capacity, current_load, current_speed, id)
        self.military = military
        self.crew_count = crew_count

    def get_total_people_count(self):
        """
        Returns the total number of people on the military ship.

        Returns:
            float: The total number of people on the military ship
            (military personnel and crew members).
        """
        return self.military + self.crew_count

    def calculate_load_time(self):
        """
            Calculates the time required to load the military ship based on the current load.

            Returns:
                float: The time required to load the military ship in minutes.
            """

        return self.current_load * 60 / 20
