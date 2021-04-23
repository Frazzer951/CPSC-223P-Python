from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D6.
die_1 = Die(6)
die_2 = Die(6)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(100_000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(1, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(
    title="Results of rolling two D6s 100,000 times and Multiplying them",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)

offline.plot({"data": data, "layout": my_layout}, filename="2d6.html")

# The reason for the gaps, is because those numbers cannot be made from multiplying an numbers in the range 1-6
# The values with larger bars, like 4, 6, and 12 are because you can get those numbers multiple ways by multiplying the numbers