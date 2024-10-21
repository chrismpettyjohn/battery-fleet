from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64

from src.sim.run import run_simulation


app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def dashboard():
    fleet, prices, batteries = run_simulation()

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

    return render_template('dashboard.html', plot_url=plot_url, fleet=fleet, batteries=batteries)


if __name__ == '__main__':
    app.run(debug=True)
