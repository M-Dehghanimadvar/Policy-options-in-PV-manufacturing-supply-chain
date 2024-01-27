import numpy as np
import json

with open('Output/New_Joule_AU_share.json') as raw_data:
    data = json.load(raw_data)

ANALYSIS_TYPES = {
    "initial_investment": ["Equipment", "Facility", "Depreciation", "Production"],
    "OpEx": ["Labour", "Electricity", "Production", "BOM", "Cell", "glass", "Al", "EVA", "JBox", "Other", "RD", "Maintenance", "Depreciation", "Income"],
    "Logistic": ["Logistic", "Logistic_cell", "Logistic_glass", "Logistic_Al", "Logistic_eva", "Logistic_jbox", "Logistic_other", "Logistic_module", "National_BOM"],
    "MSP": ["Income", "MSP"],
    "Imported": ["Module_ASP", "Logistic_Imported", "Logistic_PV_Local", "Total_logistic", "Imported_PV"]
}


def get_keys(data_set, level):
    file_path = "Output/" + data_set + ".json"
    with open(file_path) as raw_data:
        data = json.load(raw_data)
        first_level = list(data.keys())
        if level == 1:
            print(first_level)
        elif level == 2:
            second_level = {i: list(data[i].keys()) for i in first_level}
            print(second_level)
        elif level == 3:
            third_level = {i: {f: list(data[i][f].keys())} for i in first_level for f in list(data[i].keys())}
            print(third_level)


def cost_categories(analysis, cap, percentile):
    final_data = data if cap in [600000000, 1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000,
                                 7000000000, 8000000000, 9000000000, 10000000000] else None

    if final_data is None:
        print("No idea")
        return

    if analysis not in ANALYSIS_TYPES:
        print("Invalid analysis type")
        return

    cost_data = {key: np.percentile(final_data[str(cap)][key], percentile) for key in ANALYSIS_TYPES[analysis]}

    for key, value in cost_data.items():
        print(f"{key}: {value}")


# Example usage
get_keys("New_Joule_DE_share", 2)  # Adjust the file name as needed
cost_categories("MSP", 600000000, 50)
