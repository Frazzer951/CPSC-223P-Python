import matplotlib.pyplot as plt

x_values = range(0, 5001)
cubes = [x ** 3 for x in x_values]
fig, ax = plt.subplots()

ax.scatter(x_values, cubes, s=10, c=cubes, cmap=plt.cm.inferno)

plt.show()