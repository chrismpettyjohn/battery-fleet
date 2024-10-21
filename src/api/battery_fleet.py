class BatteryFleet:
    def __init__(self, batteries, max_charge_rate, max_discharge_rate):
        self.batteries = batteries
        self.max_charge_rate = max_charge_rate
        self.max_discharge_rate = max_discharge_rate
        self.revenue = 0

    def optimize(self, prices, hours=1):
        for price in prices:
            if price < 100:
                self.charge(price, hours)
            elif price > 150:
                self.discharge(price, hours)

    def charge(self, price, hours):
        available_charge = self.max_charge_rate * hours
        for battery in self.batteries:
            if available_charge <= 0:
                break
            max_possible_charge = min(battery.charge_rate * hours, battery.capacity - battery.energy_level)
            revenue_change = battery.charge(price, hours)
            available_charge -= max_possible_charge
            self.revenue += revenue_change

    def discharge(self, price, hours):
        available_discharge = self.max_discharge_rate * hours
        for battery in self.batteries:
            if available_discharge <= 0:
                break
            max_possible_discharge = min(battery.discharge_rate * hours, battery.energy_level)
            revenue_change = battery.discharge(price, hours)
            available_discharge -= max_possible_discharge
            self.revenue += revenue_change
