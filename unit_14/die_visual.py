import plotly.express as px
from die import Die

die = Die()

results = []

for roll_num in range(100):
    result = die.roll()
    results.append(result)

frequencies = []

pos_results = range(1, die.num_sides+1)

for value in pos_results:
    freq = results.count(value)
    frequencies.append(freq)

fig = px.bar(x=pos_results, y=frequencies, 
             title=f'Frequency of {die.num_sides} sided die rolls',
             labels={'x':'Possible Values', 'y':'Frequency'})
             
fig.show()