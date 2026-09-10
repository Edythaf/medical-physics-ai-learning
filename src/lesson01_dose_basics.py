#Lesson 01 - Dose Basics
#Medical physics AI learning 

prescribed_dose = 70
delivered_dose = 69.2

dose_difference = prescribed_dose - delivered_dose

print("Prescribed dose:", prescribed_dose, "Gy")
print("Delivered dose:", delivered_dose, "Gy")
print("Dose difference:", round(dose_difference,2), "Gy")

percentage_difference = (dose_difference/prescribed_dose)* 100
print("Percentage difference:", round(percentage_difference,2), "%" )

Number_of_fractions = 35

Dose_per_fraction = prescribed_dose / Number_of_fractions

print("Dose per fraction:", round(Dose_per_fraction,2), "Gy")

#Numpy dose Array

import numpy as np

#simulated dose values for several voxel

dose_values = np.array([
    68.5,
    69.2,
    70.1,
    71.0,
    69.8,
    70.5,
    68.9
])

mean_dose = np.mean(dose_values)
max_dose = np.max(dose_values)
min_dose = np.min(dose_values)

print("\nVoxel dose analysis")
print("Mean dose:", round(mean_dose, 2), "Gy")
print("Maximum dose:", round(max_dose, 2), "Gy")
print("Minimum dose:", round(min_dose, 2), "Gy")

voxels_above_70 = np.sum(dose_values >= 70)
total_voxels = dose_values.size
v70 = (voxels_above_70 / total_voxels)
print("V70:", round(v70,2), "%")

#Basic histogram of DVH 
import matplotlib.pyplot as plt

plt.hist(dose_values, bins = 5)
plt.xlabel("Dose (Gy)")
plt.ylabel("Number of Voxels")
plt.title("Dose Histogram")
plt.show()

 #simple cumulative DVH
dose_thresholds = np.linspace(
   np.min(dose_values),
   np.max(dose_values),
   100
   )

volume_percentages= []

for dose in dose_thresholds:
    volume = np.sum(dose_values >= dose) / dose_values.size *100
    volume_percentages.append(volume)

plt.plot(dose_thresholds, volume_percentages)

plt.xlabel("Dose (Gy)")
plt.ylabel("Volume (%)")
plt.title("Cumulative Dose Volume Histogram")

plt.ylim(0, 100)

plt.show()