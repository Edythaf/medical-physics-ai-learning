import numpy as np
import matplotlib.pyplot as plt

ptv_dose = np.array([
    68.5, 69.2, 69.8, 70.1, 70.4,
    70.7, 71.0, 69.9, 70.2, 70.5
])

oar_dose = np.array([
    12.0, 18.5, 22.0, 25.5, 28.0,
    31.0, 35.5, 38.0, 42.0, 45.0
])

def calculate_vx(dose_values, threshold): 
    voxels_above_threshold = np.sum(dose_values >= threshold)
    return (voxels_above_threshold / dose_values.size) *100

def calculate_dx(dose_values, volume_percent):
    percentile = 100 -volume_percent
    return np.percentile(dose_values, percentile)

def calculate_hi(dose_values): 
    d2 = calculate_dx(dose_values, 2)
    d50 = calculate_dx(dose_values, 50)
    d98 = calculate_dx(dose_values, 98)

    return (d2 - d98) / d50

def analyze_ptv(dose_values, prescription_dose):
    metrics = {
        "mean_dose" : np.mean(dose_values),
        "d98": calculate_dx(dose_values, 98),
        "d95": calculate_dx(dose_values, 95),
        "d50": calculate_dx(dose_values, 50),
        "d2": calculate_dx(dose_values, 2),
        "v_prescription": calculate_vx(dose_values, prescription_dose), 
        "hi": calculate_hi(dose_values)
    }
    return metrics

ptv_metrics = analyze_ptv(
    ptv_dose,
    prescription_dose=70
)


def analyze_oar(dose_values, vx_threshold):
   metrics = {
       "mean_dose": np.mean(dose_values), 
       "max_dose" : np.max(dose_values),
       "vx" : calculate_vx(dose_values, vx_threshold)
   } 
   return metrics

oar_metrics = analyze_oar(
    oar_dose,
    vx_threshold=30
)

def print_plan_report(ptv_metrics, oar_metrics, prescription_dose, vx_threshold):

    print("\n=== RADIOTHERAPY PLAN REPORT ===")

    print("\nPTV")
    print("Mean dose:", round(ptv_metrics["mean_dose"], 2), "Gy")
    print("D98:", round(ptv_metrics["d98"], 2), "Gy")
    print("D95:", round(ptv_metrics["d95"], 2), "Gy")
    print("D50:", round(ptv_metrics["d50"], 2), "Gy")
    print("D2:", round(ptv_metrics["d2"], 2), "Gy")
    print(
        "V" + str(prescription_dose) + ":",
        round(ptv_metrics["v_prescription"], 2),
        "%"
    )
    print("HI:", round(ptv_metrics["hi"], 3))

    print("\nOAR")
    print("Mean dose:", round(oar_metrics["mean_dose"], 2), "Gy")
    print("Maximum dose:", round(oar_metrics["max_dose"], 2), "Gy")
    print(
        "V" + str(vx_threshold) + ":",
        round(oar_metrics["vx"], 2),
        "%"
    )

print_plan_report(
    ptv_metrics,
    oar_metrics,
    prescription_dose=70,
    vx_threshold=30
)

def plot_dvh(ptv_dose, oar_dose):
    max_dose = max(np.max(ptv_dose), np.max(oar_dose))
    dose_thresholds = np.linspace(0, max_dose + 5, 200)
    ptv_volume_percentage = []
    oar_volume_percentage = []

    for dose in dose_thresholds:
        ptv_volume = calculate_vx(ptv_dose, dose)
        oar_volume = calculate_vx(oar_dose, dose)

        ptv_volume_percentage.append(ptv_volume)
        oar_volume_percentage.append(oar_volume)

    plt.plot(
        dose_thresholds,
        ptv_volume_percentage,
        label="PTV"
    )

    plt.plot(
        dose_thresholds,
        oar_volume_percentage,
        label="OAR"
    )

    plt.xlabel("Dose (Gy)")
    plt.ylabel("Volume (%)")
    plt.title("Cumulative DVH")
    plt.ylim(0, 100)
    plt.legend()
    plt.grid()

    plt.show()

plot_dvh(
    ptv_dose,
    oar_dose
)