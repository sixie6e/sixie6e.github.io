import matplotlib.pyplot as plt
import numpy as np

small_business_growth = 0.043
comm_business_growth = 0.087
x = 33300000  # num_small_business
y = 5500000  # num_comm_business
methane_23 = 1921.53  # ppb
methane_25 = 1932.67  # ppb
methane_rate = .001114
co2_23 = 419.7  # ppb
co2_25 = 422.5  # ppb
co2_rate = 0.00028
nitrogen_23 = 336.7  # ppb
nitrogen_25 = 339.9  # ppb
nitrogen_rate = 0.00032
years = 30

total_growth = (x * small_business_growth) + (y * comm_business_growth)

co2_increase = co2_25 - co2_23
methane_increase = methane_25 - methane_23
nitrogen_increase = nitrogen_25 - nitrogen_23
growth_rates = [small_business_growth, comm_business_growth, total_growth]
pollution_increases = [methane_increase, co2_increase, nitrogen_increase] 

plt.figure(figsize=(8, 6))
plt.bar(['Small Business Growth', 'Commercial Business Growth', 'Total Business Growth'], 
        pollution_increases, 
        color=['lightblue', 'lightgreen', 'orange'])
plt.xlabel('Business Growth Rate')
plt.ylabel('Pollution Increase (ppm)')
plt.title('Correlation between Business Growth and Ecological Destruction')
plt.show()


print(f"Total Business Growth: {total_growth:.2f}")
print(f"CO2 Increase: {co2_increase} ppm") 
