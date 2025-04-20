import matplotlib.pyplot as plt

from random_walk import Randomwalk

while True:
    # make random walk
    rw = Randomwalk()
    rw.fill_walk()


    # plot the points in the walk
    plt.style.use('classic')

    fig, ax = plt.subplots()

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)

    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)


    plt.show()



    user_input = input("do you want to continue? press y/n : ")
    if user_input == 'n':
        break

