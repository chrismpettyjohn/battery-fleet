from src.api.battery import Battery
from src.api.battery_fleet import BatteryFleet
from src.sim.simulate_prices import simulate_prices
from src.sim.simulate_battery import simulate_capacity, simulate_efficiency, simulate_charge_rate, simulate_discharge_rate

def run_simulation():
    # Simulate battery parameters
    batteries = [
        Battery(
            capacity=simulate_capacity(),
            charge_rate=simulate_charge_rate(),
            discharge_rate=simulate_discharge_rate(),
            efficiency=simulate_efficiency()
        )
        for _ in range(10)  # Loop 10 times to create 10 batteries
    ]

    fleet = BatteryFleet(batteries=batteries, max_charge_rate=20, max_discharge_rate=20)

    # Simulate prices and optimize the fleet operations
    prices = simulate_prices(hours=24)
    fleet.optimize(prices, hours=1)

    return fleet, prices, batteries