import matplotlib.pyplot as plt
import numpy as np

initial_pollution = 0
environmental_capacity = 1 
small_business_growth = 4.3
comm_business_growth = 8.7
x = num_small_business
y = num_comm_business
methane_23 = 1921.53
methane_25 = 1932.67
co2_23 = 419.7
co2_25 = 422.5
c02_rate = .00028
years = 30

time = np.arange(years)
pollution_levels = np.zeros(years)
pollution_levels[0] = initial_pollution

for year in range(1, years):
    pollution_levels[year] = pollution_levels[year - 1] * (1 + (4.3*x + 8.7*y))

environmental_impact = pollution_levels / environmental_capacity

plt.figure(figsize=(10, 6))
plt.plot(time, pollution_levels, label="Toxin Levels")
plt.plot(time, environmental_impact, label="Environmental Impact")
plt.xlabel("Years")
plt.ylabel("Pollution Levels / Environmental Impact")
plt.title("Impact of Industrial Growth on the Environment")
plt.legend()
plt.grid(True)
plt.show()

print("Time until industry wins: ", pollution_levels[-1])
