import numpy as np

plan_a_ptv = np.array([
    68.8, 69.5, 70.0, 70.2, 70.4,
    70.6, 70.8, 71.0, 69.9, 70.3
])

plan_a_oar = np.array([
    12.0, 18.0, 22.0, 26.0, 29.0,
    32.0, 35.0, 38.0, 41.0, 44.0
])

plan_b_ptv = np.array([
    67.5, 68.5, 69.0, 69.7, 70.0,
    70.5, 71.0, 71.5, 72.0, 72.5
])

plan_b_oar = np.array([
    8.0, 12.0, 16.0, 20.0, 24.0,
    27.0, 30.0, 32.0, 35.0, 38.0
])

def calculate_vx(dose_values, threshold):
    voxels_above_threshold = np.sum(dose_values >= threshold)
    return (voxels_above_threshold / dose_values.size) * 100

def calculate_dx(dose_values, volume_percent):
    percentile = 100 - volume_percent
    return np.percentile(dose_values, percentile)

def calculate_hi(dose_values): 
    d2 = calculate_dx(dose_values, 2)
    d98 = calculate_dx(dose_values, 98)
    d50 = calculate_dx(dose_values, 50)
    hi = (d2-d98)/d50
    return hi 

plan_a_d95 = calculate_dx(plan_a_ptv, 95)
plan_a_v70 = calculate_vx(plan_a_ptv, 70)
plan_a_hi = calculate_hi(plan_a_ptv)

plan_a_oar_mean = np.mean(plan_a_oar)
plan_a_oar_max = np.max(plan_a_oar)

plan_b_d95 = calculate_dx(plan_b_ptv, 95)
plan_b_v70 = calculate_vx(plan_b_ptv, 70)
plan_b_hi = calculate_hi(plan_b_ptv)

plan_b_oar_mean = np.mean(plan_b_oar)
plan_b_oar_max = np.max(plan_b_oar)


print("\nPLAN A")
print("D95:", round(plan_a_d95, 2), "Gy")
print("V70:", round(plan_a_v70, 2), "%")
print("HI:", round(plan_a_hi, 3))
print("OAR mean:", round(plan_a_oar_mean, 2), "Gy")
print("OAR max:", round(plan_a_oar_max, 2), "Gy")

print("\nPLAN B")
print("D95:", round(plan_b_d95, 2), "Gy")
print("V70:", round(plan_b_v70, 2), "%")
print("HI:", round(plan_b_hi, 3))
print("OAR mean:", round(plan_b_oar_mean, 2), "Gy")
print("OAR max:", round(plan_b_oar_max, 2), "Gy")

print("\nPLAN COMPARISON")

if plan_a_d95 > plan_b_d95:
    print("PTV D95: Plan A is better")
else:
    print("PTV D95: Plan B is better")

if plan_a_v70 > plan_b_v70:
    print("PTV V70: Plan A is better")
else:
    print("PTV V70: Plan B is better")

if plan_a_hi < plan_b_hi:
    print("PTV HI: Plan A is better")
else:
    print("PTV HI: Plan B is better")

if plan_a_oar_mean < plan_b_oar_mean:
    print("OAR mean dose: Plan A is better")
else:
    print("OAR mean dose: Plan B is better")

if plan_a_oar_max < plan_b_oar_max:
    print("OAR max dose: Plan A is better")
else:
    print("OAR max dose: Plan B is better")

#Simple Weighted Plan Score.
weight_d95 = 3
weight_v70 = 2
weight_hi = 1
weight_oar_mean = 2
weight_oar_max = 3

plan_a_score = 0
plan_b_score = 0

if plan_a_d95 > plan_b_d95:
    plan_a_score += weight_d95
else:
    plan_b_score += weight_d95

if plan_a_v70 > plan_b_v70:
    plan_a_score += weight_v70
else:
    plan_b_score += weight_v70

if plan_a_hi < plan_b_hi:
    plan_a_score += weight_hi
else:
    plan_b_score += weight_hi

if plan_a_oar_mean < plan_b_oar_mean:
    plan_a_score += weight_oar_mean
else:
    plan_b_score += weight_oar_mean

if plan_a_oar_max < plan_b_oar_max:
    plan_a_score += weight_oar_max
else:
    plan_b_score += weight_oar_max

print("\nWEIGHTED SCORE")
print("Plan A:", plan_a_score)
print("Plan B:", plan_b_score)