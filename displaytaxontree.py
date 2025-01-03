from pygbif import species
import tkinter as tk
from tkinter import ttk

def get_taxon_tree(scientific_name):
    try:
        species_details = species.get(scientific_name=scientific_name)
        return species_details.get('classification', [])
    except Exception as e:
        return f"Error: {e}"

def display_tree(tree):
    root = tk.Tk()
    root.title("Taxonomic Tree")

    tree_view = ttk.Treeview(root, columns=("Rank", "Name"))
    tree_view.heading("Rank", text="Rank")
    tree_view.heading("Name", text="Name")
    tree_view.column("#0", width=0)
    tree_view.column("Rank", anchor=tk.W, width=100)
    tree_view.column("Name", anchor=tk.W, width=200)
    tree_view.pack()

    def insert_node(parent, node):
        if isinstance(node, dict):
            rank = node.get('rank', '')
            name = node.get('name', '')
            tree_view.insert(parent, "end", text="", values=(rank, name), tags=("node",))
            if 'children' in node and isinstance(node['children'], list):
                for child in node['children']:
                    insert_node(tree_view.insert("", "end", text="", values=("", "")), child)
    insert_node("", tree)
    tree_view.tag_configure("node", font=("Monoid", 10), foreground ="green")
    root.mainloop()

if __name__ == "__main__":
    scientific_name = input("Enter scientific name: ")
    tree = get_taxon_tree(scientific_name)
    if tree:
        display_tree(tree)
        
        
'''
from pygbif import species
from pygbif import occurrences as o

splist = ['Mephitis mephitis', 'Drosophila melanogaster', 'Automeris io',
  'Ambystoma laterale', 'Pinnularia major', 'Gomphonema truncatum']
keys = [ species.name_backbone(x)['usageKey'] for x in splist ]
out = [ o.search(taxonKey = x, limit=0)['count'] for x in keys ] 
x = dict(zip(splist, out))
print(sorted(x.items(), key=lambda z:z[1], reverse=True))
'''
