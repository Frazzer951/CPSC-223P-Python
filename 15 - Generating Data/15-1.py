import matplotlib.pyplot as plt

cubes = [x ** 3 for x in range(5000)]
fig, ax = plt.subplots()

ax.plot(cubes, c="blue")

plt.show()