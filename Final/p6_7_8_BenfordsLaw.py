# Problem 6
import json

with open("populationbycountry.json") as f:
    data = json.load(f)

print(data)  # Get Raw Json
# print(json.dumps(data, indent=2))  # Pretty Print Json Data

# Problem 7
frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for country in data:
    population = country["population"]
    population = str(population)
    msd = int(population[0])
    frequency[msd - 1] += 1

print(frequency)

total_count = sum(frequency)
frequency_percent = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(9):
    frequency_percent[i] = frequency[i] / total_count * 100

print(frequency_percent)

# Problem 8
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Visualize the results.
x_values = list(range(1, 10))
data = [Bar(x=x_values, y=frequency_percent)]

x_axis_config = {"title": "Most Significant Digit"}
y_axis_config = {"title": "Frequency Percent of Most Significant Digit"}
my_layout = Layout(
    title="Benford’s Law using the Population of Countries",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)

offline.plot({"data": data, "layout": my_layout}, filename="BenfordsLaw.html")