import csv
from datetime import datetime  # new code

import matplotlib.pyplot as plt

filename = "data/sitka_weather_2018_simple.csv"  # new code

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, rains = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        rain = float(row[3])
        dates.append(current_date)
        rains.append(rain)

# Plot the high temperatures.
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, rains, c="red")

# Format plot.
ax.set_title("Daily Rain Inches, 2018", fontsize=24)

ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()  # new code
ax.set_ylabel("Rain Amount (in)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)

plt.show()
