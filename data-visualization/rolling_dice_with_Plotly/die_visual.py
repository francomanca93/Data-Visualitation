from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a die with 6 sides = D6
die = Die()  # instace of Die class

# Make some rolls, and store results in a list.
results = []  # A list of results
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analize the results.
frequencies = []
for value in range(1, (die.num_sides + 1)):
    frequency = results.count(value)  # .count return number of ocurrences of a value
    frequencies.append(frequency)

# Visualize the results in a Bar Chart (GRAFICO DE BARRA)

# Generating bar chart
x_values = list(range(1, die.num_sides + 1))  # Plotly doesn't accept range() so I covert the range to a list
data = [Bar(x=x_values, y=frequencies)]

# Configurating layout. Especifically the title and the axises. 
x_axis_config = {'title': 'Result'}  # Dictionary of x axis
y_axis_config = {'title': 'Frecuency of Result'}  # Dictionary of y axis
my_layout = Layout(title='Results of rolling one D6 1000 times',
    xaxis=x_axis_config,
    yaxis=y_axis_config)

# Plotting data of de roll dice in a bar chart
offline.plot({'data': data, 'layout': my_layout})
# offline.plot({'data': data, 'layout': my_layout}, filename='d6.html') # <---- To save the bar chart

