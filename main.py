"""
This script demonstrates the usage of ship-related classes and ship manager.
"""
from models.cargo_ship import CargoShip  # pylint: disable=import-error
from models.cruise_ship import CruiseShip  # pylint: disable=import-error
from models.fishing_ship import FishingShip  # pylint: disable=import-error
from models.military_ship import MilitaryShip  # pylint: disable=import-error
from managers.ship_manager import ShipManager  # pylint: disable=import-error

ships = ShipManager()
for _ in range(1):
    ships.add_ship(
        CargoShip("Serenity", "William Kidd", "Shenzhen", 46.3, 10000,
                  456, 43, 10.4, 3245, 45, "refrigerated"))
    ships.add_ship(
        CargoShip("Dreamboat", "Francis Drake", "Mangalore", 46.3, 10.000,
                  789, 45, 8, 3245, 35, "bulk"))
    ships.add_ship(
        CruiseShip("Happy Hour", "Horatio Nelson", "Mariupol", 46.3, 10000,
                   0, 45, 3245, 23, 134))
    ships.add_ship(
        CruiseShip("Carpe Diem", "Ferdinand Magellan", "Chennai", 46.3, 10000,
                   0, 40, 3245, 23, 140))
    ships.add_ship(
        MilitaryShip("Carlisle", "James Patton", "Mariupol", 46.3, 10000,
                     756, 40, 236, 35))
    ships.add_ship(
        MilitaryShip("The Alerte", "Nathaniel Crosby", "Shenzhen", 46.3, 10000,
                     789, 40, 167, 35))
    ships.add_ship(
        FishingShip("Angelica", "Asa Eldridge", "Kochi", 46.3, 10000,
                    745, 43, 43, 54))
    ships.add_ship(
        FishingShip("Talisman", "Carl Frick", "Mariupol", 46.3, 10000,
                    325, 40, 35, 59))

for ship in ships.ships:
    print(ship)

with_max_speed = ships.find_all_with_max_speed(34)
for ship in with_max_speed:
    print(ship)

same_port = ships.find_all_with_same_current_port("Mariupol")
for ship in same_port:
    print(ship)
