import numpy as np 
#PTV
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

#ptv_v70 = np.sum(ptv_dose >= 70) / ptv_dose.size * 100 this is the concept of the looping

def calculate_vx(dose_value, threshold):
    voxels_above_threshold = np.sum(dose_value >= threshold)
    volume_percentage = (voxels_above_threshold/ptv_dose.size) * 100
    return volume_percentage

print("PTV V70:", round(calculate_vx(ptv_dose, 70), 2), "%" )

def calculate_dx(dose_value, volume_percent):
    percentile = 100 - volume_percent
    dose_at_volume = np.percentile(dose_value, percentile)
    return dose_at_volume

print("PTV D95:", calculate_dx(ptv_dose, 95), "Gy")

def calculate_hi(dose_value):
    d2 = calculate_dx(dose_value, 2)
    d50 = calculate_dx(dose_value, 50)
    d98 = calculate_dx(dose_value, 98)

    hi = (d2-d98)/d50
    return hi 

ptv_hi = calculate_hi(ptv_dose)
print("PTV HI:", round(ptv_hi, 3))

def calculate_mean_dose(dose_value):
    mean_dose = np.mean(dose_value)
    return mean_dose

ptv_mean = calculate_mean_dose(ptv_dose)
print("PTV mean dose:", round(ptv_mean, 2), "Gy")

#PTV SUMMARY PART
def summarize_ptv(dose_value, prescription_dose):

    mean_dose = calculate_mean_dose(dose_value)
    d98 = calculate_dx(dose_value, 98)
    d95 = calculate_dx(dose_value, 95)
    d50 = calculate_dx(dose_value, 50)
    d2 = calculate_dx(dose_value, 2)
    v_prescription = calculate_vx(dose_value, prescription_dose)
    hi = calculate_hi(dose_value)

    print("\nPTV Plan Summary")
    print("Mean dose:", round(mean_dose, 2), "Gy")
    print("D98:", round(d98, 2), "Gy")
    print("D95:", round(d95, 2), "Gy")
    print("D50:", round(d50, 2), "Gy")
    print("D2:", round(d2, 2), "Gy")
    print(
        "V" + str(prescription_dose) + ":",
        round(v_prescription, 2),
        "%"
    )
    print("HI:", round(hi, 3))

summarize_ptv(ptv_dose, 70)

#OAR
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

def calculate_max_dose(dose_values):
    max_dose = np.max(dose_values)
    return max_dose

def summarize_oar(dose_values, vx_threshold):

    mean_dose = calculate_mean_dose(dose_values)
    max_dose = calculate_max_dose(dose_values)
    vx = calculate_vx(dose_values, vx_threshold)

    print("\nOAR Plan Summary")
    print("Mean dose:", round(mean_dose, 2), "Gy")
    print("Maximum dose:", round(max_dose, 2), "Gy")
    print(
        "V" + str(vx_threshold) + ":",
        round(vx, 2),
        "%"
    )

summarize_oar(oar_dose, 30)

summarize_ptv(ptv_dose, 70)
summarize_oar(oar_dose, 30)