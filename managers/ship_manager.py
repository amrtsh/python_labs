"""
This module defines the ShipManager class, which is responsible for managing ships.
"""
from decorators.decorator import method_calls_counter


class ShipManager:
    """A class to manage ships."""

    def __init__(self):
        """Initialize the ShipManager."""
        self.ships = []

    def __len__(self):
        """
        Get the number of ships in the ShipManager.

        Returns:
            int: The number of ships.
        """
        return len(self.ships)

    def __getitem__(self, index):
        """
        Get the ship at the specified index.

        Args:
            index (int): The index of the ship to retrieve.

        Returns:
            Ship: The ship at the specified index.
        """
        return self.ships[index]

    def __iter__(self):
        """
        Iterate over the ships in the ShipManager.

        Returns:
            iterator: An iterator over the ships.
        """
        return iter(self.ships)

    def add_ship(self, ship):
        """
        Add a ship to the managers.

        Args:
            ship (Ship): The ship object to add.
            :param ship:
            :param self:
        """
        self.ships.append(ship)

    def all_any_functions(self, port):
        """
        Check if any ship in the ShipManager has the given port,
        and if all ships have the given port.

        Args:
            port (str): The port to check.

        Returns:
            dict: A dictionary with the results of the checks:
                - 'any': True if any ship has the given port, False otherwise.
                - 'all': True if all ships have the given port, False otherwise.
        :param port:
        :return:
        """
        all_any = {"any": any(ship.current_port == port for ship in self.ships),
                   "all": all(ship.current_port == port for ship in self.ships)}
        return all_any

    @method_calls_counter
    def find_all_unloadable_ships(self):
        """
        Find all ships with a speed greater than a given maximum speed.

        Args:
            max_speed (float): The maximum speed to compare.

        Returns:
            list: A list of ships with speeds greater than max_speed.
            :param self:
        """
        print("Ships that you can unload: ")
        unloadable_ships = [ship for ship in self.ships if ship.current_load > 0]
        for ship in unloadable_ships:
            ship.unload(50)
        return unloadable_ships

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
        same_port_list = [ship for ship in self.ships if ship.current_port == current_port]
        return same_port_list
