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
  
# need to populate list with keystone species
species_data = [
    ("Bear", ["Salmon"]),
    ("Salmon", ["Krill"]),
    ("Krill", ["Copepods"]),
    ("Copepods", ["Phytoplankton", "Zooplankton"]),
    ("The entire Animal Kingdom", ["Autotrophs"])
]

ecosystem = create_ecosystem(species_data)

extinct_species = "Autotrophs" 
at_risk = check_extinction_risk(ecosystem, extinct_species)

if at_risk:
    print(f"Extinction of {extinct_species} could lead to extinction of:")
    for species in at_risk:
        print(f" - {species}")
else:
    print(f"Extinction of {extinct_species} does not directly threaten other species.")
