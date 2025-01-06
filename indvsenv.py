import matplotlib.pyplot as plt

num_small_businesses = 33300000
num_commercial_businesses = 5500000
small_business_growth_rate = 0.043
commercial_business_growth_rate = 0.087

# air
ch4_2022_ppb = 1907.53
ch4_2023_ppb = 1921.53
ch4_2024_ppb = 1932.67
ch4_growth_rate = [0.73, 0.1114]

c02_2022_ppb = 418.0
co2_2023_ppb = 419.7
co2_2024_ppb = 422.5
co2_growth_rate = [0.41, 0.77]
 
n_2023_ppb = 336.7
n_2024_ppb = 339.9
n_growth_rate = [0.95]

voc_2022_ppb = 12675.0
voc_2023_ppb = 12531.0
voc_growth_rate = -0.144

so2_2023_ppb = 100.0
so2_2024_ppb = 94.0
so2_growth_rate = -0.06

no2_2021_ppb = 53.0
no2_2022_ppb = 61.0
no2_2023_ppb = 37.0
no2_growth_rate = [0.1312, -0.39]

co_2022_MMmt = 2402
co_2023_MMmt = 2640
co_2024_MMmt = 2770
co_growth_rate = [9.02, 4.7]

o3_2022_ppb = 61
o3_2023_ppb = 84
o3_2024_ppb = 89
o3_growth_rate = [27.39, 5.62]

partmat_2022_µgm3  = 31.3
partmat_2023_µgm3 = 36.2
partmat_2024_µgm3  = 49.8
partmat_growth_rate = [13.64, 27.31]

# water
pfas_2023_ppb = 0
pfas_2024_ppb = 0
pfas_growth_rate = 0

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
