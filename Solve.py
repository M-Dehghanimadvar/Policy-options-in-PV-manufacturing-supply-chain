from pyomo.environ import SolverFactory
from Set_definitions import create_solar_model
from parameter_definitions import ParameterDefinitions
from variable_definitions import VariableDefinitions
from constraint_definitions import ConstraintDefinitions
from objective_function import ObjectiveDefinition
from pyomo.environ import *
from numpy_financial import irr
import json
import time
start_time1 = time.time()


Rate_Facility = 2.3
tax = 0.30


result_dict = {}

for i in [600000000, 1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000,
          8000000000, 9000000000, 10000000000]:
    MSP = []
    Import_Module = []
    Al = []
    Glass = []
    cell = []
    EVA = []
    JBox = []
    Other = []
    BOM = []
    Logistic = []
    National_BOM = []
    National_PV = []
    Logistic_cell = []
    Logistic_glass = []
    Logistic_Al = []
    Logistic_eva = []
    Logistic_backsheet = []
    Logistic_jbox = []
    Logistic_other = []
    Logistic_n_cell = []
    Logistic_n_glass = []
    Logistic_n_Al = []
    Logistic_n_eva = []
    Logistic_n_backsheet = []
    Logistic_n_jbox = []
    Logistic_n_other = []
    Labourr = []
    Electricity = []
    Production = []
    RD = []
    Depreciation = []
    Maintenance = []
    Incomee = []
    Logistic_module = []
    Total_Logistic = []
    Logistic_PV = []
    Logistic_PV_int = []
    Logistic_PV_nat = []
    Equip = []
    Fac = []
    for t in range(1000):
        model = create_solar_model(i, t)

        parameter_definitions = ParameterDefinitions(model, i)
        variable_definitions = VariableDefinitions(model)
        constraint_definitions = ConstraintDefinitions(model, i, Quota=1)
        objective_function = ObjectiveDefinition(model)

        opt = SolverFactory("cplex")
        results = opt.solve(model)
        National_Demand = value(sum(model.national_demand[national_market] for national_market in
                                    model.national_market))

        CapEx = (value(sum(model.module_center[potential_manufacturer] *
                           model.fixed_cost_module_center[potential_manufacturer]
                           for potential_manufacturer in model.potential_manufacturer)) / National_Demand)

        Purchasing_solar_module = value(sum(model.purchasing_solar_module[Supplier, month] *
                                            model.solar_module_purchasing_cost[Supplier, month]
                                            for Supplier in model.Supplier for month in model.month)) / National_Demand
        Purchasing_solar_cell = value(sum(model.purchasing_solar_cell[Supplier, month] *
                                          model.solar_cell_purchasing_cost[Supplier, month]
                                          for Supplier in model.Supplier for month in model.month)) / National_Demand

        Purchasing_solar_eva = value(sum(model.purchasing_solar_eva[Supplier, month] *
                                         model.solar_eva_purchasing_cost[Supplier, month]
                                         for Supplier in model.Supplier for month in model.month)) / National_Demand

        Purchasing_solar_glass = value(sum(model.purchasing_solar_glass[Supplier, month] *
                                           model.solar_glass_purchasing_cost[Supplier, month]
                                           for Supplier in model.Supplier for month in model.month)) / National_Demand
        Purchasing_solar_Al = value(sum(model.purchasing_solar_Al[Supplier, month] *
                                        model.solar_Al_purchasing_cost[Supplier, month]
                                        for Supplier in model.Supplier for month in model.month)) / National_Demand
        Purchasing_solar_jBox = value(sum(model.purchasing_solar_jBox[Supplier, month] *
                                          model.solar_jBox_purchasing_cost[Supplier, month]
                                          for Supplier in model.Supplier for month in model.month)) / National_Demand
        Purchasing_solar_SealantPottingTapeStickers = value(sum(
            model.purchasing_solar_SealantPottingTapeStickers[Supplier, month] *
            model.solar_SealantPottingTapeStickers_purchasing_cost[Supplier, month]
            for Supplier in model.Supplier for month in model.month)) / National_Demand
        Purchasing_solar_TabbingsStringingRibbons = \
            value(sum(model.purchasing_solar_TabbingsStringingRibbons[Supplier, month] *
                      model.solar_TabbingsStringingRibbons_purchasing_cost[Supplier, month]
                      for Supplier in model.Supplier for month in model.month)) / National_Demand
        Production_cost = \
            ((value(sum((model.labour_cost[potential_manufacturer] + model.electricity_cost[potential_manufacturer]) *
                        model.solar_module_production[potential_manufacturer]
                        for potential_manufacturer in model.potential_manufacturer)))) / National_Demand

        International_Transportation_In_solar_module = (value(
            sum(model.international_transportation_input_solar_module[Supplier, port, transportation_type] *
                model.international_transportation_input_cost_module[Supplier, port, transportation_type]
                for Supplier in model.Supplier for port in model.port for transportation_type in
                model.transportation_type)) + 175.8) / National_Demand
        International_Transportation_In_solar_cell = \
            (value(sum(model.international_transportation_input_solar_cell[Supplier, port, transportation_type] *
                       model.international_transportation_input_cost_cell[Supplier, port, transportation_type]
                       for Supplier in model.Supplier for port in model.port for transportation_type in
                       model.transportation_type)) + 175.8) / National_Demand
        International_Transportation_In_solar_eva = \
            (value(sum(model.international_transportation_input_solar_eva[Supplier, port, transportation_type] *
                       model.international_transportation_input_cost_eva[Supplier, port, transportation_type]
                       for Supplier in model.Supplier for port in model.port for transportation_type in
                       model.transportation_type)) + 175.8) / National_Demand
        International_Transportation_In_solar_Al = \
            (value(sum(model.international_transportation_input_solar_Al[Supplier, port, transportation_type] *
                       model.international_transportation_input_cost_Al[Supplier, port, transportation_type]
                       for Supplier in model.Supplier for port in model.port for transportation_type in
                       model.transportation_type)) + 175.8) / National_Demand
        International_Transportation_In_solar_glass = \
            (value(sum(model.international_transportation_input_solar_glass[Supplier, port, transportation_type] *
                       model.international_transportation_input_cost_glass[Supplier, port, transportation_type]
                       for Supplier in model.Supplier for port in model.port for transportation_type in
                       model.transportation_type)) + 175.8) / National_Demand
        International_Transportation_In_solar_jBox = \
            (value(sum(model.international_transportation_input_solar_jBox[Supplier, port, transportation_type] *
                       model.international_transportation_input_cost_jBox[Supplier, port, transportation_type]
                       for Supplier in model.Supplier for port in model.port for transportation_type in
                       model.transportation_type)) + 175.8) / National_Demand
        International_Transportation_In_solar_SealantPottingTapeStickers = \
            (value(sum(model.international_transportation_input_solar_SealantPottingTapeStickers[
                           Supplier, port, transportation_type] *
                       model.international_transportation_input_cost_SealantPottingTapeStickers[
                           Supplier, port, transportation_type]
                       for Supplier in model.Supplier for port in model.port for transportation_type in
                       model.transportation_type)) + 175.8) / National_Demand
        International_Transportation_In_solar_TabbingsStringingRibbons = \
            (value(sum(model.international_transportation_input_solar_TabbingsStringingRibbons[
                           Supplier, port, transportation_type] *
                       model.international_transportation_input_cost_TabbingsStringingRibbons[
                           Supplier, port, transportation_type]
                       for Supplier in model.Supplier for port in model.port for transportation_type in
                       model.transportation_type)) + 175.8) / National_Demand

        national_transportation_input_solar_module = \
            value(sum(model.national_transportation_input_solar_module[port, national_market, transportation_type] *
                      model.national_transportation_input_cost_module[port, national_market, transportation_type]
                      for port in model.port for transportation_type in model.transportation_type
                      for national_market in model.national_market)) / National_Demand
        National_Transportation_In_solar_cell = \
            value(
                sum(model.national_transportation_input_solar_cell[port, potential_manufacturer, transportation_type] *
                    model.national_transportation_input_cost_cell[port, potential_manufacturer, transportation_type]
                    for port in model.port for transportation_type in model.transportation_type
                    for potential_manufacturer in model.potential_manufacturer)) / National_Demand
        National_Transportation_In_solar_eva = \
            value(sum(model.national_transportation_input_solar_eva[port, potential_manufacturer, transportation_type] *
                      model.national_transportation_input_cost_eva[port, potential_manufacturer, transportation_type]
                      for port in model.port for transportation_type in model.transportation_type
                      for potential_manufacturer in model.potential_manufacturer)) / National_Demand

        National_Transportation_In_solar_Al = \
            value(sum(model.national_transportation_input_solar_Al[port, potential_manufacturer, transportation_type] *
                      model.national_transportation_input_cost_Al[port, potential_manufacturer, transportation_type]
                      for port in model.port for transportation_type in model.transportation_type
                      for potential_manufacturer in model.potential_manufacturer)) / National_Demand
        National_Transportation_In_solar_glass = \
            value(
                sum(model.national_transportation_input_solar_glass[port, potential_manufacturer, transportation_type] *
                    model.national_transportation_input_cost_glass[port, potential_manufacturer, transportation_type]
                    for port in model.port for transportation_type in model.transportation_type
                    for potential_manufacturer in model.potential_manufacturer)) / National_Demand
        National_Transportation_In_solar_jBox = \
            value(
                sum(model.national_transportation_input_solar_jBox[port, potential_manufacturer, transportation_type] *
                    model.national_transportation_input_cost_jBox[port, potential_manufacturer, transportation_type]
                    for port in model.port for transportation_type in model.transportation_type
                    for potential_manufacturer in model.potential_manufacturer)) / National_Demand
        National_Transportation_In_solar_SealantPottingTapeStickers = \
            value(sum(model.national_transportation_input_solar_SealantPottingTapeStickers
                      [port, potential_manufacturer, transportation_type] *
                      model.national_transportation_input_cost_SealantPottingTapeStickers
                      [port, potential_manufacturer, transportation_type]
                      for port in model.port for transportation_type in model.transportation_type
                      for potential_manufacturer in model.potential_manufacturer)) / National_Demand
        National_Transportation_In_solar_TabbingsStringingRibbons = \
            value(sum(model.national_transportation_input_solar_TabbingsStringingRibbons
                      [port, potential_manufacturer, transportation_type] *
                      model.national_transportation_input_cost_TabbingsStringingRibbons
                      [port, potential_manufacturer, transportation_type]
                      for port in model.port for transportation_type in model.transportation_type
                      for potential_manufacturer in model.potential_manufacturer)) / National_Demand

        national_transportation_out_solar_module = \
            (value(sum(model.national_transportation_out_solar_module[
                           potential_manufacturer, national_market, transportation_type] *
                       model.national_transportation_out_cost_solar_module
                       [potential_manufacturer, national_market, transportation_type]
                       for potential_manufacturer in model.potential_manufacturer for national_market in
                       model.national_market
                       for transportation_type in model.transportation_type))) / National_Demand

        Produced_Module = \
            (value((sum(
                model.national_transportation_out_solar_module[
                    potential_manufacturer, national_market, transportation_type]
                for potential_manufacturer in model.potential_manufacturer for national_market in model.national_market
                for transportation_type in model.transportation_type)))) * 545 / National_Demand

        BoM_Materials = [Purchasing_solar_cell, (Purchasing_solar_glass * 1.0), Purchasing_solar_Al,
                         Purchasing_solar_eva, Purchasing_solar_jBox, Purchasing_solar_SealantPottingTapeStickers,
                         Purchasing_solar_TabbingsStringingRibbons]

        Purchasing_BoMs = sum(BoM_Materials)
        International_Transportation = [International_Transportation_In_solar_cell,
                                        International_Transportation_In_solar_glass,
                                        International_Transportation_In_solar_Al,
                                        International_Transportation_In_solar_eva,
                                        International_Transportation_In_solar_jBox,
                                        International_Transportation_In_solar_TabbingsStringingRibbons,
                                        International_Transportation_In_solar_SealantPottingTapeStickers]

        International_Transportation_in_BoMs = sum(International_Transportation)

        National_Transportation = [National_Transportation_In_solar_cell,
                                   National_Transportation_In_solar_glass,
                                   National_Transportation_In_solar_Al,
                                   National_Transportation_In_solar_eva,
                                   National_Transportation_In_solar_jBox,
                                   National_Transportation_In_solar_TabbingsStringingRibbons,
                                   National_Transportation_In_solar_SealantPottingTapeStickers]

        National_Transportation_in_BoMs = sum(National_Transportation)

        Transportation_In = International_Transportation_in_BoMs + National_Transportation_in_BoMs

        Trade_Cost_BoM = Purchasing_BoMs * (value(model.import_tariff_BoMs))

        BoM_without_others = [Purchasing_solar_Al, Purchasing_solar_eva, (Purchasing_solar_glass),
                              Purchasing_solar_jBox,
                              ]
        wihtout = sum(BoM_without_others)
        Trade_Cost_BoM_without = wihtout * (value(model.import_tariff_BoMs))

        Labour_cost = ((value(sum((model.labour_cost[potential_manufacturer]) *
                                  model.solar_module_production[potential_manufacturer]
                                  for potential_manufacturer in model.potential_manufacturer)))) / National_Demand
        Electricity_cost = value(sum(model.electricity_cost[potential_manufacturer] *
                                     model.solar_module_production[potential_manufacturer] for
                                     potential_manufacturer in model.potential_manufacturer)) / National_Demand

        Equipment = CapEx * 1.3 * 0.625

        Facility = CapEx * Rate_Facility * 0.375

        Depreciation_equipment = Equipment / 7
        Depreciation_facility = Facility / 20

        maintenance = Equipment * 0.04

        Trade_Cost_Module = Purchasing_solar_module * (value(model.import_tariff_module))

        import_module = Purchasing_solar_module + International_Transportation_In_solar_module + \
                        national_transportation_input_solar_module + Trade_Cost_Module

        Working_Capital = (Production_cost + Purchasing_BoMs) * 0.25

        Initial_Investment = Working_Capital + Equipment + Facility

        variable_cost = Transportation_In + Production_cost + Purchasing_BoMs + national_transportation_out_solar_module


        Selling_price = []
        Selling_price_low = 0.01
        Selling_price_high = 0.7
        for t in range(20):
            Selling_price = (Selling_price_low + Selling_price_high) / 2
            R_and_D_SGA = (Selling_price - Purchasing_solar_cell) * 0.13
            Final_cost = variable_cost + R_and_D_SGA + Depreciation_equipment + Depreciation_facility + maintenance
            Income = (Selling_price - Final_cost)
            Profit_margin = (Income / Selling_price) * 100
            Tax = tax * Income
            Cash_flow = variable_cost + R_and_D_SGA + maintenance + Tax
            IRR = irr([-(Initial_Investment),
                       (Selling_price - Cash_flow), (Selling_price - Cash_flow),
                       (Selling_price - Cash_flow),
                       (Selling_price - Cash_flow), (Selling_price - Cash_flow),
                       (Selling_price - Cash_flow),
                       (Selling_price - (Cash_flow - Working_Capital))])
            if 0.138 <= IRR <= 0.142:
                break
            elif IRR < 0.14:
                Selling_price_low = Selling_price
            else:
                Selling_price_high = Selling_price

        MSP.append(Selling_price)
        # Import_Module.append(import_module)
        Al.append(Purchasing_solar_Al)
        Glass.append(Purchasing_solar_glass)
        cell.append(Purchasing_solar_cell)
        EVA.append(Purchasing_solar_eva)
        JBox.append(Purchasing_solar_jBox)
        Other.append(Purchasing_solar_SealantPottingTapeStickers + Purchasing_solar_TabbingsStringingRibbons)
        BOM.append(Purchasing_BoMs)
        Logistic.append(International_Transportation_in_BoMs)
        National_BOM.append(National_Transportation_in_BoMs)
        Logistic_module.append(national_transportation_out_solar_module)
        Total_Logistic.append(
            International_Transportation_in_BoMs + National_Transportation_in_BoMs + national_transportation_out_solar_module)
        Logistic_cell.append(International_Transportation_In_solar_cell)
        Logistic_glass.append(International_Transportation_In_solar_glass)
        Logistic_Al.append(International_Transportation_In_solar_Al)
        Logistic_eva.append(International_Transportation_In_solar_eva)
        Logistic_jbox.append(International_Transportation_In_solar_jBox)
        Logistic_other.append(
            International_Transportation_In_solar_TabbingsStringingRibbons + International_Transportation_In_solar_SealantPottingTapeStickers)
        Labourr.append(Labour_cost)
        Electricity.append(Electricity_cost)
        Production.append(Production_cost)
        RD.append(R_and_D_SGA)
        Depreciation.append(Depreciation_facility + Depreciation_equipment)
        Equip.append(Equipment)
        Fac.append(Facility)
        Maintenance.append(maintenance)
        Incomee.append(float(Income))
        Logistic_PV.append(International_Transportation_In_solar_module + national_transportation_input_solar_module)
        Logistic_PV_int.append(International_Transportation_In_solar_module)
        Logistic_PV_nat.append(national_transportation_input_solar_module)

        result_dict[str(int(i))] = {
            "MSP": MSP,
            "Cell": cell,
            "Glass": Glass,
            "Al": Al,
            "EVA": EVA,
            "JBox": JBox,
            "Other": Other,
            "BOM": BOM,
            "Logistic": Logistic,
            'National_BOM':National_BOM,
            "Total_Logistic": Total_Logistic,
            "Logistic_cell": Logistic_cell,
            "Logistic_glass": Logistic_glass,
            "Logistic_Al": Logistic_Al,
            "Logistic_jbox": Logistic_jbox,
            "Logistic_eva": Logistic_eva,
            "Logistic_other": Logistic_other,
            "Logistic_module":Logistic_module,
            "Labour": Labourr,
            "Electricity": Electricity,
            "Production": Production,
            "RD": RD,
            "Depreciation": Depreciation,
            "Equipment": Equip,
            "Facility": Fac,
            "Maintenance": Maintenance,
            "Income": Incomee,
        }

        with open("Output/New_Joule_AU_share.json", "w") as file_object:
            json.dump(result_dict, file_object, indent=4)
    print("--- %s seconds ---" % (time.time() - start_time1), "Cap: ", i)