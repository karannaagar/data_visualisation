import matplotlib.pyplot as plt

from random_walk import Randomwalk

# make random walk
rw = Randomwalk()
rw.fill_walk()


# plot the points in the walk
plt.style.use('classic')

fig, ax = plt.subplots()

ax.scatter(rw.x_values, rw.y_values)

plt.show()

