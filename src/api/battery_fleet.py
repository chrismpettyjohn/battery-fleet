import numpy as np

class BatteryFleet:
    def __init__(self, batteries, max_charge_rate, max_discharge_rate):
        self.batteries = batteries
        self.max_charge_rate = max_charge_rate
        self.max_discharge_rate = max_discharge_rate
        self.revenue = 0
        self.price_history = []

    def calculate_thresholds(self, battery):
        discharge_ratio = battery.discharge_rate / battery.capacity
        charge_ratio = battery.charge_rate / battery.capacity

        # Lower charge threshold and higher discharge threshold for low discharge rate batteries
        charge_threshold = 70 + 20 * (1 - discharge_ratio)
        discharge_threshold = 130 - 20 * (1 - discharge_ratio)

        return charge_threshold, discharge_threshold

    def optimize(self, prices, hours=1, forecast_window=24):
        for i, price in enumerate(prices):
            self.price_history.append(price)
            if len(self.price_history) > 168:  # Keep a week's worth of hourly prices
                self.price_history.pop(0)

            avg_price = np.mean(self.price_history)
            future_prices = prices[i:i + forecast_window]

            for battery in self.batteries:
                charge_threshold, discharge_threshold = self.calculate_thresholds(battery)

                # Look-ahead for high-capacity, low-discharge batteries
                if battery.discharge_rate / battery.capacity < 0.05 and len(future_prices) > 0:
                    max_future_price = max(future_prices)
                    if max_future_price > discharge_threshold and battery.energy_level / battery.capacity < 0.9:
                        continue  # Skip discharging to save for future high price

                if price < charge_threshold and price < avg_price:
                    self.charge(price, hours, [battery])
                elif price > discharge_threshold or (
                        price > avg_price and battery.energy_level / battery.capacity > 0.7):
                    self.discharge(price, hours, [battery])

    def charge(self, price, hours, batteries):
        total_possible_charge = sum(min(b.charge_rate * hours, b.capacity - b.energy_level) for b in batteries)
        available_charge = min(self.max_charge_rate * hours, total_possible_charge)

        for battery in sorted(batteries, key=lambda b: b.charge_rate / b.capacity):
            max_charge = min(battery.charge_rate * hours, battery.capacity - battery.energy_level, available_charge)
            revenue_change = battery.charge(price, max_charge)
            self.revenue += revenue_change
            available_charge -= max_charge
            if available_charge <= 0:
                break

    def discharge(self, price, hours, batteries):
        total_possible_discharge = sum(min(b.discharge_rate * hours, b.energy_level) for b in batteries)
        available_discharge = min(self.max_discharge_rate * hours, total_possible_discharge)

        for battery in sorted(batteries, key=lambda b: (b.discharge_rate / b.capacity, b.energy_level / b.capacity),
                              reverse=True):
            max_discharge = min(battery.discharge_rate * hours, battery.energy_level, available_discharge)
            revenue_change = battery.discharge(price, max_discharge)
            self.revenue += revenue_change
            available_discharge -= max_discharge
            if available_discharge <= 0:
                break
