import csv
from datetime import datetime
from os import stat

import matplotlib.pyplot as plt

filename = "data/death_valley_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    min = float("inf")
    max = float("-inf")
    name = ""
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:  # new code
            high = int(row[4])
            low = int(row[5])
            name = row[1]

            if high > max:
                max = high
            if low < min:
                min = low

        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# Plot the high and low temperatures.
plt.style.use("seaborn")
fig, ax = plt.subplots()

ax.plot(dates, highs, c="red", alpha=0.5)  # new code
ax.plot(dates, lows, c="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)


# Format plot.
title = f"Daily high and low temperatures - 2018\n{name}"  # new code
ax.set_title(title, fontsize=20)

ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)

plt.ylim([min - 10, max + 10])

plt.show()
