import json
import matplotlib.pyplot as plt
from datetime import datetime

# Explore the structure of the data.
filename = "data/deathsbystateovertime.json"
with open(filename, encoding="utf-8") as f:
    json_data = json.load(f)

data = json_data["data"]

dates, total_deaths = [], []

for row in data:
    if row[9] == "CA":
        try:
            current_date = datetime.fromisoformat(row[8])
            deaths = int(row[15])

        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            total_deaths.append(deaths)

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.set_title("California Covid Deaths", fontsize=20)

ax.bar(dates, total_deaths, color="blue")
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Total Deaths")

plt.show()
