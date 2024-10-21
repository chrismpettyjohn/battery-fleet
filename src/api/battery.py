class Battery:
    def __init__(self, capacity, charge_rate, discharge_rate, efficiency):
        self.capacity = capacity
        self.charge_rate = charge_rate
        self.discharge_rate = discharge_rate
        self.efficiency = efficiency
        self.energy_level = 0

    def charge(self, price, hours):
        max_possible_charge = min(self.charge_rate * hours * self.efficiency, self.capacity - self.energy_level)
        self.energy_level += max_possible_charge
        return max_possible_charge * -price

    def discharge(self, price, hours):
        max_possible_discharge = min(self.discharge_rate * hours, self.energy_level)
        self.energy_level -= max_possible_discharge
        return max_possible_discharge * price
