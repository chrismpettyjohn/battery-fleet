from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64

from src.api import simulate_prices

app = Flask(__name__)

@app.route('/')
def dashboard():
    img = io.BytesIO()

    # Generate a simple plot of energy prices over time
    hours = list(range(24))
    prices = simulate_prices(24)
    plt.plot(hours, prices, label="Energy Prices")
    plt.xlabel('Hour')
    plt.ylabel('Price ($/MWh)')
    plt.title('Energy Prices Over Time')
    plt.legend()

    # Save plot to the BytesIO object
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return render_template('dashboard.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)

