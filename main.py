from models.cargo_ship import CargoShip
from models.cruise_ship import CruiseShip
from models.fishing_ship import FishingShip
from models.military_ship import MilitaryShip
from managers.ship_manager import ShipManager

ships = ShipManager()
for _ in range(7):
    ships.add_ship(CargoShip(10.4, "Serenity", "William Kidd", "Shenzhen", 46.3, 10.000,
                             456, 43, 3245, 45, "refrigerated"))
    ships.add_ship(CargoShip(8.0, "Dreamboat", "Francis Drake", "Mangalore", 46.3, 10.000, 789, 45, 3245, 35, "bulk"))
    ships.add_ship(CruiseShip("Happy Hour", "Horatio Nelson", "Mariupol", 46.3, 10.000, 0, 45, 3245, 23, 134))
    ships.add_ship(CruiseShip("Carpe Diem", "Ferdinand Magellan", "Chennai", 46.3, 10.000, 0, 40, 3245, 23, 140))
    ships.add_ship(MilitaryShip("Carlisle", "James Patton", "Mariupol", 46.3, 10.000, 756, 40, 236, 35))
    ships.add_ship(MilitaryShip("The Alerte", "Nathaniel Crosby", "Shenzhen", 46.3, 10.000, 789, 40, 167, 35))
    ships.add_ship(FishingShip("Angelica", "Asa Eldridge", "Kochi", 46.3, 10.000, 745, 43, 43, 54))
    ships.add_ship(FishingShip("Talisman", "Carl Frick", "Mariupol", 46.3, 10.000, 325, 40, 35, 59))

for ship in ships.ships:
    print(ship)

with_max_speed = ships.find_all_with_max_speed(34)
for ship in with_max_speed:
    print(ship)

same_port = ships.find_all_with_same_current_port("Mariupol")
for ship in same_port:
    print(ship)
