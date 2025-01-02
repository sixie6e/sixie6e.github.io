import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

G = nx.DiGraph()
source = "Source"
G.add_node(source)
kingdoms = [ "Animalia", "Archaea", "Bacteria", "Chromista", "Fungi", "Plantae", "Protista"] 
for kingdom in kingdoms:
    G.add_node(kingdom)
    G.add_edge(source, kingdom)

node_sizes = [200] * len(kingdoms) 

def update(val):
    global node_sizes
    slider_values = [slider.val for slider in sliders] 
    for i in range(len(kingdoms)):
        node_sizes[i] = max(10, min(slider_values[i], 1000 - sum(slider_values[:i]) - sum(slider_values[i+1:]))) 
    nx.draw(G, pos=pos, node_size=2, with_labels=True, font_size=8)
    plt.draw()

fig, ax = plt.subplots()
sliders = []
for i, kingdom in enumerate(kingdoms):
    slider_ax = plt.axes([0.1, 0.1 + 0.05 * i, 0.8, 0.02])
    slider = Slider(slider_ax, kingdom, 0, 1000, valinit=node_sizes[i], color='green')
    slider.on_changed(update)
    sliders.append(slider)

pos = nx.spring_layout(G) 
nx.draw(G, pos=pos, node_size=2, with_labels=True, font_size=8)

plt.show()
