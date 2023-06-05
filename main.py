"""
This script demonstrates the usage of ship-related classes and ship manager.
"""
from managers import ship_manager, set_manager
from models.cargo_ship import CargoShip  # pylint: disable=import-error
from models.cruise_ship import CruiseShip  # pylint: disable=import-error
from models.fishing_ship import FishingShip  # pylint: disable=import-error
from models.military_ship import MilitaryShip  # pylint: disable=import-error

ships = ship_manager.ShipManager()
for _ in range(1):
    ships.add_ship(
        CargoShip("Serenity", "William Kidd", "Shenzhen", 46.3, 10000,
                  456, 43, 3245, 45, "refrigerated", 8))
    ships.add_ship(
        CargoShip("Dreamboat", "Francis Drake", "Mangalore", 46.3, 10.000,
                  789, 45, 3245, 35, "bulk"))
    ships.add_ship(
        CruiseShip("Happy Hour", "Horatio Nelson", "Mariupol", 46.3, 10000,
                   0, 45, 3245, 23, 134, 13))
    ships.add_ship(
        CruiseShip("Carpe Diem", "Ferdinand Magellan", "Chennai", 46.3, 10000,
                   0, 40, 3245, 23, 140))
    ships.add_ship(
        MilitaryShip("Carlisle", "James Patton", "Mariupol", 46.3, 10000,
                     756, 40, 236, 35))
    ships.add_ship(
        MilitaryShip("The Alerte", "Nathaniel Crosby", "Shenzhen", 46.3, 10000,
                     789, 40, 167, 35, 24))
    ships.add_ship(
        FishingShip("Angelica", "Asa Eldridge", "Kochi", 46.3, 10000,
                    745, 43, 43, 54))
    ships.add_ship(
        FishingShip("Talisman", "Carl Frick", "Mariupol", 46.3, 10000,
                    325, 40, 35, 59))

for ship in ships.ships:
    print(ship)

unloadable_ships = ships.find_all_unloadable_ships()
for ship in unloadable_ships:
    print(ship)

same_port = ships.find_all_with_same_current_port("Mariupol")
for ship in same_port:
    print(ship)

ship_list = len(ships)
print("Number of ships:", ship_list)

get_item_index = ships[4]
print("Ship at index 4:", get_item_index)

get_total_people_count_list = [ship.get_total_people_count() for ship in ships]
print(get_total_people_count_list)

print("Function enumerate: ")
for count, ship in enumerate(ships, 1):
    print(count, ship)

print("Function zip: ")
for i in zip(ships, get_total_people_count_list):
    print(i)

print("Dict comprehension: ")
for i in ships:
    print(i.get_attributes(int))

print("All and any functins: ")
print(ships.all_any_functions("Mariupol"))

print("Iter (set_manager): ")
ship_power = set_manager.SetManager(ships)
for power in ship_power:
    print(power)

print("Length (set_manager): ")
print(len(ship_power))

print("Index (set_manager): ")
print(ship_power[7])

ships[0].load(9999)
