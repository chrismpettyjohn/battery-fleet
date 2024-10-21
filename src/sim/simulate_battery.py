import random

def simulate_capacity(min_capacity=50, max_capacity=200):
    """Simulates battery capacity in MWh."""
    return random.uniform(min_capacity, max_capacity)

def simulate_charge_rate(min_rate=5, max_rate=15):
    """Simulates battery charge rate in MW."""
    return random.uniform(min_rate, max_rate)

def simulate_discharge_rate(min_rate=5, max_rate=15):
    """Simulates battery discharge rate in MW."""
    return random.uniform(min_rate, max_rate)

def simulate_efficiency(min_efficiency=0.85, max_efficiency=0.95):
    """Simulates battery efficiency as a percentage."""
    return random.uniform(min_efficiency, max_efficiency)
