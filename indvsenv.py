import matplotlib.pyplot as plt

num_small_businesses = 33300000
num_commercial_businesses = 5500000
small_business_growth_rate = 0.043
commercial_business_growth_rate = 0.087

ch4_2022_ppb = 1907.53
ch4_2023_ppb = 1921.53
ch4_2024_ppb = 1932.67
ch4_growth_rate = [0.73, 0.1114]

co2_2022_ppb = 418.0
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

pb_2023_ppb = 0
pb_2024_ppb = 0
pb_growth_rate = 0

eto_2023_ppb = 0
eto_2024_ppb = 0
eto_growth_rate = 0

c10h8_2023_ppb = 0
c10h8_2024_ppb = 0
c10h8_growth_rate = 0

bap_2023_ppb = 0
bap_2024_ppb = 0
bap_growth_rate = 0

tph_2023_ppb = 0
tph_2024_ppb = 0
tph_growth_rate = 0

btex_2023_ppb = 0
btex_2024_ppb = 0
btex_growth_rate = 0

mtbe_2023_ppb = 0
mtbe_2024_ppb = 0
mtbe_growth_rate = 0

tba_2023_ppb = 0
tba_2024_ppb = 0
tba_growth_rate = 0

total_business_growth = (
    num_small_businesses * small_business_growth_rate 
    + num_commercial_businesses * commercial_business_growth_rate
)

ch4_increase = (ch4_2024_ppb - ch4_2023_ppb) * ch4_growth_rate
co2_increase = (co2_2024_ppb - co2_2023_ppb) * co2_growth_rate
n_increase = (n_2024_ppb - n_2023_ppb) * n_growth_rate
c0_increase = (c0_2024_MMmt - c0_2023_MMmt) * c0_growth_rate
so2_increase = (so2_2024_ppb - so2_2023_ppb) * so2_growth_rate
no2_increase = (no2_2024_ppb - no2_2023_ppb) * no2_growth_rate
pfas_increase = (pfas_2024_ppb - pfas_2023_ppb) * pfas_growth_rate
voc_increase = (voc_2024_ppb - voc_2023_ppb) * voc_growth_rate
o3_increase = (o3_2024_ppb - o3_2023_ppb) * o3_growth_rate
partmat_increase = (partmat_2024_µgm3 - partmat_2023_µgm3) * partmat_growth_rate
hg_increase = (hg_2024_ppb - hg_2023_ppb) * hg_growth_rate
cd_increase = (cd_2024_ppb - cd_2023_ppb) * cd_growth_rate
as_increase = (as_2024_ppb - as_2023_ppb) * as_growth_rate
pb_increase = (pb_2024_ppb - pb_2023_ppb) * pb_growth_rate
eto_increase = (eto_2024_ppb - eto_2023_ppb) * eto_growth_rate
c10h8_increase = (c10h8_2024_µgm3 - c10h8_2023_µgm3) * c10h8_growth_rate
bap_increase = (bap_2024_ppb - bap_2023_ppb) * bap_growth_rate
tph_increase = (tph_2024_ppb - tph_2023_ppb) * tph_growth_rate
btex_increase = (btex_2024_ppb - btex_2023_ppb) * btex_growth_rate
mtbe_increase = (mtbe_2024_ppb - mtbe_2023_ppb) * mtbe_growth_rate
tba_increase = (tba_2024_ppb - tba_2023_ppb) * tba_growth_rate

growth_rates = [
    small_business_growth_rate, 
    commercial_business_growth_rate, 
    total_business_growth 
]

pollution_increases = [ch4_increase, co2_increase, n_increase, co_increase, so2_increase, no2_increase, pfas_increase, voc_increase, o3_increase, partmat_increase, hg_increase, cd_increase, as_increase, pb_increase, eto_increase, c10h8_increase, bap_increase, tph_increase, btex_increase, mtbe_increase, tba_increase]

plt.figure(figsize=(8, 6))
plt.bar(
    ['Small Business Growth', 'Commercial Business Growth', 'Total Business Growth'], 
    pollution_increases, 
    color=['lightblue', 'lightgreen', 'orange']
)
plt.xlabel('Business Growth Rate')
plt.ylabel('Pollution Increase') # need to fix to include ppm and µgm3 
plt.title('Correlation between Business Growth and Pollution Increases') 
plt.show()

print(f"Total Business Growth: {total_business_growth:.2f}")
print(f"Particulate Matter Increase: {partmat_increase:.4f} µgm3")
print(f"CH4 Increase: {ch4_increase:.4f} ppb")
print(f"CO2 Increase: {co2_increase:.4f} ppb")
print(f"N Increase: {n_increase:.4f} ppb")
print(f"CO Increase: {co_increase:.4f} MMmt")
print(f"SO2 Increase: {so2_increase:.4f} ppb")
print(f"NO2 Increase: {no2_increase:.4f} ppb")
print(f"PFAS Increase: {pfas_increase:.4f} ppb")
print(f"VOC Increase: {voc_increase:.4f} ppb")
print(f"O3 Increase: {o3_increase:.4f} ppb") 
print(f"Hg Increase: {hg_increase:.4f} ppb") 
print(f"Cd Increase: {cd_increase:.4f} ppb")
print(f"As Increase: {as_increase:.4f} ppb")
print(f"Pb Increase: {pb_increase:.4f} ppb") 
print(f"EtO Increase: {eto_increase:.4f} ppb")
print(f"C10H8 Increase: {c10h8_increase:.4f} ppb") 
print(f"BaP Increase: {bap_increase:.4f} ppb") 
print(f"TPH Increase: {tph_increase:.4f} ppb")
print(f"BTEX Increase: {btex_increase:.4f} ppb")
print(f"MTBE Increase: {mtbe_increase:.4f} ppb") 
print(f"tBA Increase: {tba_increase:.4f} ppb")
