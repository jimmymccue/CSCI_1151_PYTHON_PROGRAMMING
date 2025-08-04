import matplotlib.pyplot as plt

ind_var = range(1, 10001)
dep_var = [x * x for x in ind_var]
plt.style.use('dark_background')
figure, graph = plt.subplots()
graph.scatter(ind_var, dep_var, s=10, c=dep_var, cmap=plt.cm.Purples)
graph.set_title('Square Numbers', fontsize=14, loc='left')
graph.set_xlabel('Value', fontsize=14)
graph.set_ylabel('Square Values', fontsize=14)
graph.tick_params(labelsize=14)
graph.axis([1,10000, 1,100_000_000])
graph.ticklabel_format(axis= 'y', style='plain')

# plt.show()
plt.savefig('simple_s quares_graph.png', bbox_inches='tight', pad_inches=0.5)