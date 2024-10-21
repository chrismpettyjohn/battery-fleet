import random
import numpy as np

class Battery:
    def __init__(self, capacity, charge_rate, discharge_rate, efficiency):
        self.capacity = capacity
        self.charge_rate = charge_rate
        self.discharge_rate = discharge_rate
        self.efficiency = efficiency
        self.energy_level = 0

    def charge(self, price):
        charge_amount = min(self.charge_rate * self.efficiency, self.capacity - self.energy_level)
        self.energy_level += charge_amount
        return charge_amount * -price

    def discharge(self, price):
        discharge_amount = min(self.discharge_rate, self.energy_level)
        self.energy_level -= discharge_amount
        return discharge_amount * price

class BatteryFleet:
    def __init__(self, batteries, max_charge_rate, max_discharge_rate):
        self.batteries = batteries
        self.max_charge_rate = max_charge_rate
        self.max_discharge_rate = max_discharge_rate
        self.revenue = 0

    def optimize(self, prices):
        for price in prices:
            if price < 100:  # Heuristic: Charge when prices are low
                self.charge(price)
            elif price > 150:  # Heuristic: Discharge when prices are high
                self.discharge(price)

    def charge(self, price):
        available_charge = self.max_charge_rate
        for battery in self.batteries:
            if available_charge <= 0:
                break
            revenue_change = battery.charge(price)
            available_charge -= battery.charge_rate
            self.revenue += revenue_change

    def discharge(self, price):
        available_discharge = self.max_discharge_rate
        for battery in self.batteries:
            if available_discharge <= 0:
                break
            revenue_change = battery.discharge(price)
            available_discharge -= battery.discharge_rate
            self.revenue += revenue_change

def simulate_prices(hours=24):
    prices = []
    for hour in range(hours):
        if 6 <= hour <= 9 or 18 <= hour <= 21:
            prices.append(random.uniform(150, 250))
        else:
            prices.append(random.uniform(50, 100))
    return prices

# Example setup
batteries = [
    Battery(capacity=100, charge_rate=10, discharge_rate=8, efficiency=0.9),
    Battery(capacity=120, charge_rate=12, discharge_rate=9, efficiency=0.92)
]

fleet = BatteryFleet(batteries=batteries, max_charge_rate=20, max_discharge_rate=20)
prices = simulate_prices()
fleet.optimize(prices)

print("Total revenue:", fleet.revenue)

