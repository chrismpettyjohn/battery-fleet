from api.battery_fleet import BatteryFleet
from api.battery import Battery
from sim.simulate_prices import simulate_prices
from web.site import app  # Importing the Flask app


def run_simulation():
    # Set up the battery fleet
    batteries = [
        Battery(capacity=100, charge_rate=10, discharge_rate=8, efficiency=0.9),
        Battery(capacity=120, charge_rate=12, discharge_rate=9, efficiency=0.92)
    ]
    fleet = BatteryFleet(batteries=batteries, max_charge_rate=20, max_discharge_rate=20)

    # Simulate prices and optimize the fleet operations
    prices = simulate_prices(hours=24)
    fleet.optimize(prices, hours=1)

    print(f"Total revenue: {fleet.revenue}")
    for idx, battery in enumerate(batteries):
        print(f"Battery {idx + 1} final energy level: {battery.energy_level:.2f} MWh")


if __name__ == "__main__":
    # Run both the simulation and the Flask web server
    run_simulation()
    app.run(debug=True)
