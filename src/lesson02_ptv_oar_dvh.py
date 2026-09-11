import numpy as np
import matplotlib.pyplot as plt

ptv_dose = np.array([
    68.5,
    69.2,
    69.8,
    70.1,
    70.4,
    70.7,
    71.0,
    69.9,
    70.2,
    70.5
])

oar_dose = np.array([
     12.0,
    18.5,
    22.0,
    25.5,
    28.0,
    31.0,
    35.5,
    38.0,
    42.0,
    45.0
])

ptv_mean = np.mean(ptv_dose)
ptv_max = np.max(ptv_dose)
ptv_min = np.min(ptv_dose)

oar_mean = np.mean(oar_dose)
oar_max = np.max(oar_dose)
oar_min = np.min(oar_dose)

print("PTV mean dose:", round(ptv_mean, 2), "Gy")
print("PTV max dose:", round(ptv_max, 2), "Gy")
print("PTV min dose:", round(ptv_min, 2), "Gy")

print("\nOAR mean dose:", round(oar_mean, 2), "Gy")
print("OAR max dose:", round(oar_max, 2), "Gy")
print("OAR min dose:", round(oar_min, 2), "Gy")

dose_threshold = np.linspace(0,75,200)
ptv_volume_percentage = []
oar_volume_percentage = []

for dose in dose_threshold:
    ptv_voxels = np.sum(ptv_dose >= dose)
    ptv_volume = (ptv_voxels / ptv_dose.size) * 100
    ptv_volume_percentage.append(ptv_volume)

    oar_voxels = np.sum(oar_dose >= dose)
    oar_volume = (oar_voxels / oar_dose.size) * 100
    oar_volume_percentage.append(oar_volume)

plt.plot(
    dose_threshold, 
    ptv_volume_percentage,
    label = "PTV"
)

plt.plot(
    dose_threshold,
    oar_volume_percentage, 
    label = "OAR"
)

plt.xlabel("Dose (Gy)")
plt.ylabel("Volume (%)")
plt.title("PTV vs OAR Cumulative DVH")
plt.xlim(0,75)
plt.ylim(0,100)

plt.legend()
plt.grid()
plt.show()

#V90 dan D95

ptv_v70 = np.sum(ptv_dose >= 70)/ptv_dose.size * 100
ptv_d95 = np.percentile(ptv_dose, 5)

print("PTV V70:", round(ptv_v70, 2), "%")
print("PTV D95:", round(ptv_d95, 2), "Gy")

ptv_d98 = np.percentile(ptv_dose, 2)
ptv_d50 = np.percentile(ptv_dose, 50)
ptv_d2 = np.percentile(ptv_dose, 98)

print("\nPTV dose metrics")
print("D98:", round(ptv_d98, 2), "Gy")
print("D50:", round(ptv_d50, 2), "Gy")
print("D2:", round(ptv_d2, 2), "Gy")

#Homogeneity Index
homogeneity_index = (ptv_d2 - ptv_d98)/ptv_d50
print("HI:", np.around(homogeneity_index * 100, 3), "%")

#OAR evaluation.
oar_mean = np.mean(oar_dose)
oar_max = np.max(oar_dose)

oar_v30 = (
    np.sum(oar_dose >= 30) / oar_dose.size
) * 100

print("\nOAR dose metrics")
print("Dmean:", round(oar_mean, 2), "Gy")
print("Dmax:", round(oar_max, 2), "Gy")
print("V30:", round(oar_v30, 2), "%")