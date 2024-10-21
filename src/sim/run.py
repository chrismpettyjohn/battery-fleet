from src.api.battery import Battery
from src.api.battery_fleet import BatteryFleet
from src.sim.simulate_prices import simulate_prices
from src.sim.simulate_battery import simulate_capacity, simulate_efficiency, simulate_charge_rate, simulate_discharge_rate

def run_simulation():
    batteries = []
    for _ in range(10):
        capacity = simulate_capacity()
        charge_rate = simulate_charge_rate()
        discharge_rate = simulate_discharge_rate()
        efficiency_percentage = simulate_efficiency() * 100  # Simulate efficiency as a percentage
        efficiency_fraction = efficiency_percentage / 100  # Convert to fraction
        battery = Battery(capacity, charge_rate, discharge_rate, efficiency_fraction)
        batteries.append(battery)

    fleet = BatteryFleet(batteries=batteries, max_charge_rate=20, max_discharge_rate=20)

    # Simulate prices and optimize the fleet operations
    prices = simulate_prices(hours=24)
    fleet.optimize(prices, hours=1)

    return fleet, prices, batteries