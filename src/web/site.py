from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64

from src.sim.simulate_prices import simulate_prices

app = Flask(__name__)

@app.route('/')
def dashboard():
    prices = simulate_prices(24)
    img = io.BytesIO()

    # Plot energy prices
    plt.plot(range(24), prices, label="Energy Prices")
    plt.xlabel('Hour')
    plt.ylabel('Price ($/MWh)')
    plt.title('Energy Prices Over 24 Hours')
    plt.legend()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return render_template('dashboard.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
