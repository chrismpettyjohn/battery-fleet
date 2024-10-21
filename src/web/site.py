from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64
from src.sim.run import run_simulation

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def dashboard():
    fleet, _, batteries = run_simulation()

    # Prepare image buffer
    img = io.BytesIO()

    # Create a larger plot
    plt.figure(figsize=(12, 6))  # Larger figure size

    # Plot profit history for each battery
    for i, battery in enumerate(batteries):
        plt.plot(
            range(len(battery.profit_history)), battery.profit_history,
            label=f"Battery {i + 1}: {round(battery.capacity, 2)} MWh"
        )

    plt.xlabel('Hour')
    plt.ylabel('Profit ($)')
    plt.title('Battery Profits Over 24 Hours')

    # Adjust legend
    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1), borderaxespad=0.)

    # Save plot to the image buffer
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)

    # Convert image to base64 for embedding in HTML
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    # Pass plot_url and battery data to the template
    return render_template('dashboard.html', plot_url=plot_url, fleet=fleet, batteries=batteries)


if __name__ == '__main__':
    app.run(debug=True)
