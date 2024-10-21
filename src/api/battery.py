class Battery:
    def __init__(self, capacity, charge_rate, discharge_rate, efficiency):
        self.capacity = capacity
        self.charge_rate = charge_rate
        self.discharge_rate = discharge_rate
        self.efficiency = efficiency
        self.energy_level = 0
        self.profit = 0
        self.profit_history = []  # To keep track of all profits over time

    def charge(self, price, amount):
        actual_charge = min(amount, self.capacity - self.energy_level)
        cost = actual_charge * price
        self.energy_level += actual_charge
        self.profit -= cost
        self.profit_history.append(self.profit)  # Record the current profit
        return -cost

    def discharge(self, price, amount):
        actual_discharge = min(amount, self.energy_level)
        revenue = actual_discharge * price * self.efficiency
        self.energy_level -= actual_discharge
        self.profit += revenue
        self.profit_history.append(self.profit)  # Record the current profit
        return revenue
