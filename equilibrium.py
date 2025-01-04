import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import tkinter as tk
from collections import defaultdict

class Species:
    def __init__(self, name, dependencies=[]):
        self.name = name
        self.dependencies = dependencies

def create_ecosystem(species_data):
    ecosystem = {}
    for name, dependencies in species_data:
        ecosystem[name] = Species(name, dependencies)
    return ecosystem

def check_extinction_risk(ecosystem, extinct_species):
    at_risk = []
    for species_name, species in ecosystem.items():
        if extinct_species in species.dependencies:
            at_risk.append(species_name)
    return at_risk
  
# need to populate this list with keystone species
species_data = [
    ("Bear", ["Salmon"]),
    ("Salmon", ["Krill"]),
    ("Krill", ["Copepods"]),
    ("Copepods", ["Phytoplankton", "Zooplankton"]),
    ("Most of the Animal Kingdom", ["Autotrophs"])
]

def on_slider_change(event):
    global sliders
    slider_index = sliders.index(event.widget)
    change = event.widget.get() - event.widget.prev_value

    if slider_index > 0:
        sliders[slider_index - 1].set(sliders[slider_index - 1].get() - change)
    if slider_index < len(sliders) - 1:
        sliders[slider_index + 1].set(sliders[slider_index + 1].get() + change)
        
    event.widget.prev_value = event.widget.get()

def build_dependency_graph(filename):
  graph = defaultdict(list)
  with open(filename, 'r') as f:
    for line in f:
      dependent, source = line.strip().split()
      graph[source].append(dependent)
  return graph

def find_direct_dependencies(graph, source_species):
  return graph[source_species][:3] 

def display_dependencies(source_species, dependencies):
  print(f"{source_species}")
  print("Dependencies:")
  for i, dependency in enumerate(dependencies):
    print(f"{i+1}. {dependency}")
      
window = tk.Tk()
window.title("Equilibrium")
canvas = tk.Canvas(window, width=300, height=70)
canvas.pack()
sliders = []
for i in range(7):
    slider = tk.Scale(window, from_=0, to=100000, orient=tk.HORIZONTAL, label=f"Species {i+1}", activebackground='green')
    slider.pack()
    slider.prev_value = 0
    slider.bind("<B1-Motion>", on_slider_change)
    sliders.append(slider)

sliders[0].set(15141)
sliders[1].set(47867)
sliders[2].set(17411)
sliders[3].set(14)
sliders[4].set(444)
sliders[5].set(27271)
sliders[6].set(45244)

window.mainloop()

ecosystem = create_ecosystem(species_data)
extinct_species = "Autotrophs"  # need to change to take slider position data after adjustment
at_risk = check_extinction_risk(ecosystem, extinct_species)

if at_risk:
    print(f"Extinction of {extinct_species} could lead to extinction of:")
    for species in at_risk:
        print(f" - {species}")
else:
    print(f"Extinction of {extinct_species} does not DIRECTLY threaten other species.")

if __name__ == "__main__":
    dependency_file = "speciesdep.txt"
    graph = build_dependency_graph(dependency_file)
    source_species = input("Enter species in the following format: 'Genus species'")
    dependencies = find_direct_dependencies(graph, source_species)
    display_dependencies(source_species, dependencies) 
