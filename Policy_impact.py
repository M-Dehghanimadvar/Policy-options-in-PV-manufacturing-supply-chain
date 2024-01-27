import numpy as np
import json
import os
from numpy_financial import irr


def load_joule_data(file_path):
    """Load Joule data from JSON file."""
    with open(file_path) as raw_data:
        return json.load(raw_data)


def calculate_trade_cost(component, tariff):
    """Calculate trade cost for a given component and tariff."""
    return component * tariff


def calculate_irr_analysis(analysis, selling_price, Labour, final_cost, income, tax, cash_flow, initial_investment, Labour_incentives, Working_Capital):
    """Calculate IRR-based or sensitivity analysis."""
    if analysis == "IRR":
        return irr([-initial_investment,
                    (selling_price - (cash_flow - (Labour * Labour_incentives))),
                    (selling_price - cash_flow),
                    (selling_price - cash_flow),
                    (selling_price - cash_flow),
                    (selling_price - cash_flow),
                    (selling_price - cash_flow),
                    (selling_price - (cash_flow - Working_Capital))])
    else:
        return irr([-initial_investment,
                    (selling_price - (cash_flow - (Labour * Labour_incentives))),
                    (selling_price - cash_flow),
                    (selling_price - cash_flow),
                    (selling_price - cash_flow),
                    (selling_price - cash_flow),
                    (selling_price - cash_flow),
                    (selling_price - (cash_flow - Working_Capital))])

def main(Capacity):
    # Configuration
    output_folder = "/Users/z5263438/Codes/Code Python/Share with Joule/Output/"
    filename = "New_Joule_DE_share.json"
    file_path = os.path.join(os.getcwd(), output_folder, filename)

    # Load Joule data
    data_Joule = load_joule_data(file_path)

    policy = np.arange(0.00, 0.1, 0.002)
    zero_list = [0.0 for _ in range(len(policy))]

    Equipment_incentives = zero_list
    Facility_incentives = zero_list
    Labour_incentives = zero_list
    Electricity_incentives = zero_list
    Tax_incentives = zero_list
    Module_incentives = policy

    import_tariff_module = zero_list
    import_tariff_cell = zero_list
    import_tariff_glass = zero_list
    import_tariff_Al = zero_list
    import_tariff_eva = zero_list
    import_tariff_jBox = zero_list
    import_tariff_other = zero_list

    MSP = []
    IRRR = []

    tax = 0.15
    analysis = "IRR"

    for t in range(len(Module_incentives)):
        for s in range(2):
            i = Capacity

            Equipment = data_Joule[str(i)]["Equipment"][s] - \
                        (data_Joule[str(i)]["Equipment"][s] * Equipment_incentives[t])

            dep_equipment = Equipment / 7

            Facility = data_Joule[str(i)]["Facility"][s] - \
                        (data_Joule[str(i)]["Facility"][s] * Facility_incentives[t])

            dep_facility = Facility / 20

            maintenance = data_Joule[str(i)]["Maintenance"][s]

            Trade_Cost_Module = (data_Joule["PV Module ASP"][s]) * import_tariff_module[t]

            import_module = data_Joule["PV Module ASP"][s] + data_Joule["Logistic_PV"][s]

            import_module_median = np.percentile(data_Joule["PV Module ASP"], 50) + \
                                   np.percentile(data_Joule["Logistic_PV"], 50)

            import_module_low = np.percentile(data_Joule["PV Module ASP"], 10) + \
                                np.percentile(data_Joule["Logistic_PV"], 10)

            import_module_high = np.percentile(data_Joule["PV Module ASP"], 90) + \
                                 np.percentile(data_Joule["Logistic_PV"], 90)

            Glass = data_Joule[str(i)]["Glass"][s]

            Al = data_Joule[str(i)]["Al"][s]

            cell = data_Joule[str(i)]["Cell"][s]

            eva = data_Joule[str(i)]["EVA"][s]

            jBox = data_Joule[str(i)]["JBox"][s]

            Other = data_Joule[str(i)]["Other"][s]

            BOM = Glass + eva + jBox + Other + cell + Al

            Glass_Trade = Glass * import_tariff_glass[t]

            Al_Trade = Al * import_tariff_Al[t]

            cell_Trade = cell * import_tariff_cell[t]

            eva_Trade = eva * import_tariff_eva[t]

            jBox_Trade = jBox * import_tariff_jBox[t]

            Other_Trade = Other * import_tariff_other[t]

            Trade_Cost_BoM = Glass_Trade + Al_Trade + cell_Trade + eva_Trade + jBox_Trade + Other_Trade

            Labour = data_Joule[str(i)]["Labour"][s]

            Electricity = data_Joule[str(i)]["Electricity"][s] - \
                          ((data_Joule[str(i)]["Electricity"][s]) * Electricity_incentives[t])

            Production = Electricity + Labour

            Working_Capital = (Electricity + (Labour - (Labour * Labour_incentives[t])) + BOM) * 0.25

            Initial_Investment = Working_Capital + Facility + Equipment

            Logistic = data_Joule[str(i)]["Total_Logistic"][s]

            variable_cost = Logistic + Production + BOM + Trade_Cost_BoM - Module_incentives[t]

            Depreciation = dep_equipment + dep_facility

            if analysis == "IRR":
                Selling_price = import_module_median
                R_and_D_SGA = data_Joule[str(i)]["RD"][s]
                Final_cost = variable_cost + R_and_D_SGA + Depreciation + maintenance
                Income = (Selling_price - Final_cost)

                if (tax - (tax * Tax_incentives[t])) * Income < 0:
                    Tax = 0
                else:
                    Tax = (tax - (tax * Tax_incentives[t])) * Income
                Cash_flow = variable_cost + R_and_D_SGA + maintenance + Tax

                IRR = calculate_irr_analysis(analysis, Selling_price,Labour, Final_cost, Income , Tax, Cash_flow,
                             Initial_Investment, Labour_incentives[t], Working_Capital)


            else:

                Selling_price = []
                for Selling_price in np.arange(0.25, 2, 0.00001):
                    R_and_D_SGA = data_Joule[str(i)]["RD"][s]

                    Final_cost = variable_cost + R_and_D_SGA + Depreciation + maintenance - Module_incentives[t]
                    Income = (Selling_price - Final_cost)
                    Tax = (tax - (tax * Tax_incentives[t])) * Income
                    Cash_flow = variable_cost + R_and_D_SGA + maintenance + Tax

                    IRR = calculate_irr_analysis(analysis, Selling_price, Labour, Final_cost, Income, Tax, Cash_flow,
                                                 Initial_Investment, Labour_incentives[t], Working_Capital)
                    if 0.138 <= IRR <= 0.142:
                        break
                    else:
                        continue

            IRRR.append(IRR * 100)
            MSP.append(Selling_price)
    
        print(IRRR, ",")
        print(MSP, ",")
        IRRR = []
        MSP = []

if __name__ == "__main__":
    main(Capacity)
