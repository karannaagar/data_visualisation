from die import Die
from plotly.graph_objs import Bar, Layout

from plotly import offline



# create a D6
die = Die()

# make some rolls
results= []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# analyse the results 
frequencies=[]
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)


# visualize the results

x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'result'}
y_axis_config = {'title': 'frequency of result'}

my_layout = Layout(title='results of rolling 1000 times', xaxis = x_axis_config, yaxis = y_axis_config)

offline.plot({'data' : data , 'layout' : my_layout}, filename='d6.html')