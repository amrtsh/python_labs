"""
This module defines the ShipManager class, which is responsible for managing ships.
"""


class ShipManager:
    """A class to manage ships."""

    def __init__(self):
        """Initialize the ShipManager."""
        self.ships = []

    def add_ship(self, ship):
        """
        Add a ship to the managers.

        Args:
            ship (Ship): The ship object to add.
            :param ship:
            :param self:
        """
        self.ships.append(ship)

    def find_all_with_max_speed(self, max_speed):
        """
        Find all ships with a speed greater than a given maximum speed.

        Args:
            max_speed (float): The maximum speed to compare.

        Returns:
            list: A list of ships with speeds greater than max_speed.
            :param max_speed:
            :param self:
        """
        print(f"Ships whose speed is greater than {max_speed} :")
        max_speed_list = [ship for ship in self.ships
                          if ship.set_speed(ship.current_speed) > max_speed]
        return max_speed_list

    def find_all_with_same_current_port(self, current_port):
        """
        Find all ships with the same current port as the given port.

        Args:
            current_port (str): The current port to compare.

        Returns:
            list: A list of ships with the same current port as current_port.
            :param current_port:
            :param self:
        """
        print(f"Ships whose port matches {current_port}")
        same_port_list = [ship for ship in self.ships if ship.dock() == current_port]
        return same_port_list
