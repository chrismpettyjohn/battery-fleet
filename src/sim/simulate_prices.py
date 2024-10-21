import random

def simulate_prices(hours=24):
    prices = []
    for hour in range(hours):
        if 6 <= hour <= 9 or 18 <= hour <= 21:
            prices.append(random.uniform(150, 250))
        else:
            prices.append(random.uniform(50, 100))
    return prices
