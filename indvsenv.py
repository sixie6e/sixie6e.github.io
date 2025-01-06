import matplotlib.pyplot as plt

num_small_businesses = 33300000
num_commercial_businesses = 5500000
small_business_growth_rate = 0.043
commercial_business_growth_rate = 0.087

# air
ch4_2023_ppb = 1921.53
ch4_2024_ppb = 1932.67
ch4_growth_rate = 0.001114

co2_2023_ppb = 419.7
co2_2024_ppb = 422.5
co2_growth_rate = 0.00028

n_2023_ppb = 336.7
n_2024_ppb = 339.9
n_growth_rate = 0.00032

voc_2023_ppb = 0
voc_2024_ppb = 0
voc_growth_rate = 0

so2_2023_ppb = 0
so2_2024_ppb = 0
so2_growth_rate = 0

no2_2023_ppb = 0
no2_2024_ppb = 0
no2_growth_rate = 0

# water
PFAS_2023_ppb = 0
PFAS_2024_ppb = 0
PFAS_growth_rate = 0

hg_2023_ppb = 0
hg_2024_ppb = 0
hg_growth_rate = 0

cd_2023_ppb = 0
cd_2024_ppb = 0
cd_growth_rate = 0

as_2023_ppb = 0
as_2024_ppb = 0
as_growth_rate = 0

eto_2023_ppb = 0
eto_2024_ppb = 0
eto_growth_rate = 0

pb_2023_ppb = 0
pb_2024_ppb = 0
pb_growth_rate = 0

total_business_growth = (
    num_small_businesses * small_business_growth_rate 
    + num_commercial_businesses * commercial_business_growth_rate
)

ch4_increase = (ch4_2024_ppb - ch4_2023_ppb) * ch4_growth_rate
co2_increase = (co2_2024_ppb - co2_2023_ppb) * co2_growth_rate
n_increase = (n_2024_ppb - n_2023_ppb) * n_growth_rate

growth_rates = [
    small_business_growth_rate, 
    commercial_business_growth_rate, 
    total_business_growth 
]

pollution_increases = [ch4_increase, co2_increase, n_increase]

plt.figure(figsize=(8, 6))
plt.bar(
    ['Small Business Growth', 'Commercial Business Growth', 'Total Business Growth'], 
    pollution_increases, 
    color=['lightblue', 'lightgreen', 'orange']
)
plt.xlabel('Business Growth Rate')
plt.ylabel('Pollution Increase (ppb)')
plt.title('Correlation between Business Growth and Pollution Increases') 
plt.show()

print(f"Total Business Growth: {total_business_growth:.2f}")
print(f"ch4 Increase: {ch4_increase:.4f} ppb")
print(f"CO2 Increase: {co2_increase:.4f} ppb")
print(f"Nitrogen Increase: {n_increase:.4f} ppb") 
