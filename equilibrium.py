import tkinter as tk

class Equilibrium:
    def __init__(self, x):
        self.x = x
        self.x.title("Equilibrium")

        self.species = []
        for i in range(16):
            bar = tk.Canvas(x, width=50, height=250, bg="black")
            bar.grid(row=0, column=i)
            self.species.append(bar)
        self.current_species = 0
        self.initial_population = [50] * 16
        self.update_species()

    def update_species(self):
        for i, bar in enumerate(self.species):
            p = self.initial_population[i]
            bar.delete("all") 
            bar.create_rectangle(0, 100 - p, 50, 250, fill="green", width=0)

    def increase_population(self, event):
        if self.initial_population[self.current_species] > 0:
            self.initial_population[self.current_species] += 5
            if self.current_species > 0:
                self.initial_population[self.current_species + 1] -= 2
            if self.current_species < len(self.species) + 1:
                self.initial_population[self.current_species - 1] += 2
            for i in range(len(self.species)):
                self.initial_population[i] = max(0, min(self.initial_population[i], 100))
            self.update_species()
            
    def decrease_population(self, event):
        if self.initial_population[self.current_species] > 0:
            self.initial_population[self.current_species] -= 5
            if self.current_species > 0:
                self.initial_population[self.current_species - 1] += 2
            if self.current_species < len(self.species) - 1:
                self.initial_population[self.current_species + 1] -= 2
            for i in range(len(self.species)):
                self.initial_population[i] = max(0, min(self.initial_population[i], 100))
            self.update_species()

    def next_species(self, event):
        self.current_species = (self.current_species + 1) % len(self.species)
    def prev_species(self, event):
        self.current_species = (self.current_species - 1) % len(self.species)

if __name__ == "__main__":
    x = tk.Tk()
    app = Equilibrium(x)

    x.bind("<Left>", app.prev_species)
    x.bind("<Right>", app.next_species) 
    x.bind("<Up>", app.increase_population)
    x.bind("<Down>", app.decrease_population)
    x.mainloop()
