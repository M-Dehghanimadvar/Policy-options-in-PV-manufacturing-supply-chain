import numpy as np
from Joule_database_US import *

Number_of_manufacturer = candidate_location.iloc[0]["Number_of_Locations"]


def info():
    """
    Considering BoM separately may not be correct, because in this case,
    the economies of scale would not apply to BoM.
    Transportation - updated
    Learning Rate = 10%-27%
    Scaling factor = -0.07 – -0.21
    """


def Objective_Function(model):
    Fixed_Cost_o = sum(model.module_center[potential_manufacturer] *
                       model.fixed_cost_module_center[potential_manufacturer]
                       for potential_manufacturer in model.potential_manufacturer)
    Purchasing_solar_module_o = sum(model.purchasing_solar_module[suppliers, month] * (1 + model.import_tariff_module) *
                                    model.solar_module_purchasing_cost[suppliers, month]
                                    for suppliers in model.Supplier for month in model.month)
    Purchasing_solar_cell_o = sum(model.purchasing_solar_cell[suppliers, month] * (1 + model.import_tariff_BoMs) *
                                  model.solar_cell_purchasing_cost[suppliers, month]
                                  for suppliers in model.Supplier for month in model.month)
    Purchasing_solar_eva_o = sum(model.purchasing_solar_eva[suppliers, month] * (1 + model.import_tariff_BoMs) *
                                 model.solar_eva_purchasing_cost[suppliers, month]
                                 for suppliers in model.Supplier for month in model.month)
    Purchasing_solar_glass_o = sum(model.purchasing_solar_glass[suppliers, month] * (1 + model.import_tariff_BoMs) *
                                   model.solar_glass_purchasing_cost[suppliers, month]
                                   for suppliers in model.Supplier for month in model.month)
    Purchasing_solar_Al_o = sum(model.purchasing_solar_Al[suppliers, month] * (1 + model.import_tariff_BoMs) *
                                model.solar_Al_purchasing_cost[suppliers, month]
                                for suppliers in model.Supplier for month in model.month)
    Purchasing_solar_jBox_o = sum(model.purchasing_solar_jBox[suppliers, month] * (1 + model.import_tariff_BoMs) *
                                  model.solar_jBox_purchasing_cost[suppliers, month]
                                  for suppliers in model.Supplier for month in model.month)
    Purchasing_solar_SealantPottingTapeStickers_o = sum(
        model.purchasing_solar_SealantPottingTapeStickers[suppliers, month] * (1 + model.import_tariff_BoMs) *
        model.solar_SealantPottingTapeStickers_purchasing_cost[suppliers, month]
        for suppliers in model.Supplier for month in model.month)
    Purchasing_solar_TabbingsStringingRibbons_o = sum(
        model.purchasing_solar_TabbingsStringingRibbons[suppliers, month] *
        (1 + model.import_tariff_BoMs) *
        model.solar_TabbingsStringingRibbons_purchasing_cost[
            suppliers, month]
        for suppliers in model.Supplier for month in model.month)

    Production_cost_o = sum(
        (model.labour_cost[potential_manufacturer] + model.electricity_cost[potential_manufacturer]) *
        model.solar_module_production[potential_manufacturer]
        for potential_manufacturer in model.potential_manufacturer)

    International_Transportation_In_solar_module_o = \
        sum(model.international_transportation_input_solar_module[suppliers, port, transportation_type] *
            model.international_transportation_input_cost_module[suppliers, port, transportation_type]
            for suppliers in model.Supplier for port in model.port for transportation_type in
            model.transportation_type)
    International_Transportation_In_solar_cell_o = \
        sum(model.international_transportation_input_solar_cell[suppliers, port, transportation_type] *
            model.international_transportation_input_cost_cell[suppliers, port, transportation_type]
            for suppliers in model.Supplier for port in model.port for transportation_type in
            model.transportation_type)
    International_Transportation_In_solar_eva_o = \
        sum(model.international_transportation_input_solar_eva[suppliers, port, transportation_type] *
            model.international_transportation_input_cost_eva[suppliers, port, transportation_type]
            for suppliers in model.Supplier for port in model.port for transportation_type in
            model.transportation_type)
    International_Transportation_In_solar_Al_o = \
        sum(model.international_transportation_input_solar_Al[suppliers, port, transportation_type] *
            model.international_transportation_input_cost_Al[suppliers, port, transportation_type]
            for suppliers in model.Supplier for port in model.port for transportation_type in
            model.transportation_type)
    International_Transportation_In_solar_glass_o = \
        sum(model.international_transportation_input_solar_glass[suppliers, port, transportation_type] *
            model.international_transportation_input_cost_glass[suppliers, port, transportation_type]
            for suppliers in model.Supplier for port in model.port for transportation_type in
            model.transportation_type)
    International_Transportation_In_solar_jBox_o = \
        sum(model.international_transportation_input_solar_jBox[suppliers, port, transportation_type] *
            model.international_transportation_input_cost_jBox[suppliers, port, transportation_type]
            for suppliers in model.Supplier for port in model.port for transportation_type in
            model.transportation_type)
    International_Transportation_In_solar_SealantPottingTapeStickers_o = \
        sum(model.international_transportation_input_solar_SealantPottingTapeStickers[
                suppliers, port, transportation_type] *
            model.international_transportation_input_cost_SealantPottingTapeStickers[
                suppliers, port, transportation_type]
            for suppliers in model.Supplier for port in model.port for transportation_type in
            model.transportation_type)
    International_Transportation_In_solar_TabbingsStringingRibbons_o = \
        sum(model.international_transportation_input_solar_TabbingsStringingRibbons[
                suppliers, port, transportation_type] *
            model.international_transportation_input_cost_TabbingsStringingRibbons[suppliers, port, transportation_type]
            for suppliers in model.Supplier for port in model.port for transportation_type in
            model.transportation_type)
    National_Transportation_In_solar_module_o = \
        sum(model.national_transportation_input_solar_module[port, national_market, transportation_type] *
            model.national_transportation_input_cost_module[port, national_market, transportation_type]
            for port in model.port for transportation_type in model.transportation_type
            for national_market in model.national_market)
    National_Transportation_In_solar_cell_o = \
        sum(model.national_transportation_input_solar_cell[port, potential_manufacturer, transportation_type] *
            model.national_transportation_input_cost_cell[port, potential_manufacturer, transportation_type]
            for port in model.port for transportation_type in model.transportation_type
            for potential_manufacturer in model.potential_manufacturer)
    National_Transportation_In_solar_eva_o = \
        sum(model.national_transportation_input_solar_eva[port, potential_manufacturer, transportation_type] *
            model.national_transportation_input_cost_eva[port, potential_manufacturer, transportation_type]
            for port in model.port for transportation_type in model.transportation_type
            for potential_manufacturer in model.potential_manufacturer)
    National_Transportation_In_solar_Al_o = \
        sum(model.national_transportation_input_solar_Al[port, potential_manufacturer, transportation_type] *
            model.national_transportation_input_cost_Al[port, potential_manufacturer, transportation_type]
            for port in model.port for transportation_type in model.transportation_type
            for potential_manufacturer in model.potential_manufacturer)
    National_Transportation_In_solar_glass_o = \
        sum(model.national_transportation_input_solar_glass[port, potential_manufacturer, transportation_type] *
            model.national_transportation_input_cost_glass[port, potential_manufacturer, transportation_type]
            for port in model.port for transportation_type in model.transportation_type
            for potential_manufacturer in model.potential_manufacturer)
    National_Transportation_In_solar_jBox_o = \
        sum(model.national_transportation_input_solar_jBox[port, potential_manufacturer, transportation_type] *
            model.national_transportation_input_cost_jBox[port, potential_manufacturer, transportation_type]
            for port in model.port for transportation_type in model.transportation_type
            for potential_manufacturer in model.potential_manufacturer)
    National_Transportation_In_solar_SealantPottingTapeStickers_o = \
        sum(model.national_transportation_input_solar_SealantPottingTapeStickers
            [port, potential_manufacturer, transportation_type] *
            model.national_transportation_input_cost_SealantPottingTapeStickers
            [port, potential_manufacturer, transportation_type]
            for port in model.port for transportation_type in model.transportation_type
            for potential_manufacturer in model.potential_manufacturer)
    National_Transportation_In_solar_TabbingsStringingRibbons_o = \
        sum(model.national_transportation_input_solar_TabbingsStringingRibbons
            [port, potential_manufacturer, transportation_type] *
            model.national_transportation_input_cost_TabbingsStringingRibbons
            [port, potential_manufacturer, transportation_type]
            for port in model.port for transportation_type in model.transportation_type
            for potential_manufacturer in model.potential_manufacturer)

    national_transportation_out_solar_module_o = \
        sum(model.national_transportation_out_solar_module[
                potential_manufacturer, national_market, transportation_type] *
            model.national_transportation_out_cost_solar_module
            [potential_manufacturer, national_market, transportation_type]
            for potential_manufacturer in model.potential_manufacturer for national_market in model.national_market
            for transportation_type in model.transportation_type)
    Purchasing_BoMs_o = Purchasing_solar_cell_o + Purchasing_solar_Al_o + Purchasing_solar_eva_o + \
                        Purchasing_solar_glass_o + Purchasing_solar_jBox_o + \
                        Purchasing_solar_SealantPottingTapeStickers_o + \
                        Purchasing_solar_TabbingsStringingRibbons_o
    International_Transportation_in_BoMs_o = International_Transportation_In_solar_cell_o + \
                                             International_Transportation_In_solar_Al_o + \
                                             International_Transportation_In_solar_eva_o + \
                                             International_Transportation_In_solar_jBox_o + \
                                             International_Transportation_In_solar_TabbingsStringingRibbons_o + \
                                             International_Transportation_In_solar_glass_o + \
                                             International_Transportation_In_solar_SealantPottingTapeStickers_o
    National_Transportation_in_BoMs_o = National_Transportation_In_solar_cell_o \
                                        + National_Transportation_In_solar_Al_o + \
                                        National_Transportation_In_solar_eva_o + \
                                        National_Transportation_In_solar_jBox_o + \
                                        National_Transportation_In_solar_TabbingsStringingRibbons_o + \
                                        National_Transportation_In_solar_glass_o + \
                                        National_Transportation_In_solar_SealantPottingTapeStickers_o
    Transportation_In_o = International_Transportation_in_BoMs_o + National_Transportation_in_BoMs_o
    R_and_D_SGA_o = ((national_transportation_out_solar_module_o * 0.25) - Purchasing_solar_cell_o) * 0.13
    Depreciation_cost_o = Fixed_Cost_o / 7
    maintenance_o = Fixed_Cost_o * 0.04
    import_module_o = Purchasing_solar_module_o + International_Transportation_In_solar_module_o + \
                      National_Transportation_In_solar_module_o
    return Fixed_Cost_o + Purchasing_BoMs_o + Transportation_In_o + R_and_D_SGA_o + Depreciation_cost_o + maintenance_o + \
           import_module_o + Production_cost_o


def Get_Previous_Month(month):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    if month == "Jan":
        return None
    return months[months.index(month) - 1]


Quota = 1  # 0 means 0% from China, 0.5 means 50% from China


def International_Module_Capacity(model, Supplier, Quota):
    if Supplier == "China":
        """The amount of purchased Module should be equal or less than supplier Capacity"""
        return sum(model.purchasing_solar_module[Supplier, month] for month in model.month) <= \
               (sum(model.solar_module_capacity[Supplier, month] for month in model.month)) * Quota
    return sum(model.purchasing_solar_module[Supplier, month] for month in model.month) <= \
           (sum(model.solar_module_capacity[Supplier, month] for month in model.month))


def International_cell_Capacity(model, Supplier, Quota):
    """The amount of purchased Module should be equal or less than supplier Capacity"""
    if Supplier == "China":
        return sum(model.purchasing_solar_cell[Supplier, month] for month in model.month) <= \
               sum(model.solar_cell_capacity[Supplier, month] for month in model.month) * Quota
    return sum(model.purchasing_solar_cell[Supplier, month] for month in model.month) <= \
           sum(model.solar_cell_capacity[Supplier, month] for month in model.month)


def International_Al_Capacity(model, Supplier, Quota):
    """The amount of purchased Module should be equal or less than supplier Capacity"""
    if Supplier == "China":
        return sum(model.purchasing_solar_Al[Supplier, month] for month in model.month) <= \
               sum(model.solar_Al_capacity[Supplier, month] for month in model.month) * Quota
    return sum(model.purchasing_solar_Al[Supplier, month] for month in model.month) <= \
           sum(model.solar_Al_capacity[Supplier, month] for month in model.month)


def International_Glass_Capacity(model, Supplier, Quota):
    """The amount of purchased Module should be equal or less than supplier Capacity"""
    if Supplier == "China":
        return sum(model.purchasing_solar_glass[Supplier, month] for month in model.month) <= \
               sum(model.solar_glass_capacity[Supplier, month] for month in model.month) * Quota
    return sum(model.purchasing_solar_glass[Supplier, month] for month in model.month) <= \
           sum(model.solar_glass_capacity[Supplier, month] for month in model.month)


def International_EVA_Capacity(model, Supplier, Quota):
    """The amount of purchased Module should be equal or less than supplier Capacity"""
    if Supplier == "China":
        return sum(model.purchasing_solar_eva[Supplier, month] for month in model.month) <= \
               sum(model.solar_eva_capacity[Supplier, month] for month in model.month) * Quota
    return sum(model.purchasing_solar_eva[Supplier, month] for month in model.month) <= \
           sum(model.solar_eva_capacity[Supplier, month] for month in model.month)



def International_JBox_Capacity(model, Supplier, Quota):
    """The amount of purchased Module should be equal or less than supplier Capacity"""
    if Supplier == "China":
        return sum(model.purchasing_solar_jBox[Supplier, month] for month in model.month) <= \
               sum(model.solar_JBox_capacity[Supplier, month] for month in model.month) * Quota
    return sum(model.purchasing_solar_jBox[Supplier, month] for month in model.month) <= \
           sum(model.solar_JBox_capacity[Supplier, month] for month in model.month)


def International_TabbingsStringingRibbons_Capacity(model, Supplier, Quota):
    """The amount of purchased Module should be equal or less than supplier Capacity"""
    if Supplier == "China":
        return sum(model.purchasing_solar_TabbingsStringingRibbons[Supplier, month] for month in model.month) <= \
               sum(model.solar_TabbingsStringingRibbons_capacity[Supplier, month] for month in model.month) * Quota
    return sum(model.purchasing_solar_TabbingsStringingRibbons[Supplier, month] for month in model.month) <= \
           sum(model.solar_TabbingsStringingRibbons_capacity[Supplier, month] for month in model.month)


def International_SealantPottingTapeStickers_Capacity(model, Supplier, Quota):
    """The amount of purchased Module should be equal or less than supplier Capacity"""
    if Supplier == "China":
        return sum(model.purchasing_solar_SealantPottingTapeStickers[Supplier, month] for month in model.month) <= \
               sum(model.solar_SealantPottingTapeStickers_capacity[Supplier, month] for month in model.month) * Quota
    return sum(model.purchasing_solar_SealantPottingTapeStickers[Supplier, month] for month in model.month) <= \
           sum(model.solar_SealantPottingTapeStickers_capacity[Supplier, month] for month in model.month)


def International_Transport_In_Module(model, Supplier):
    """The amount of purchased Module should be equal to amount Module transport to the potential_manufacturer"""
    return sum(model.purchasing_solar_module[Supplier, month] for month in model.month) >= \
           sum(model.international_transportation_input_solar_module[Supplier, port, transportation_type]
               for port in model.port for transportation_type in model.transportation_type)


def National_Transport_In_Module(model, port):
    """The amount of Module transport from potential_manufacturer to the market should be equal to the amount of Module received at the
    potential_manufacturer """
    return sum(model.international_transportation_input_solar_module[Supplier, port, transportation_type]
               for Supplier in model.Supplier for transportation_type in model.transportation_type) >= \
           sum(model.national_transportation_input_solar_module[port, national_market, transportation_type]
               for national_market in model.national_market for transportation_type in
               model.transportation_type)


def International_Transport_In_cell(model, Supplier):
    """The amount of purchased cell should be equal to amount cell transport to the potential_manufacturer"""
    return sum(model.purchasing_solar_cell[Supplier, month] for month in model.month) >= \
           sum(model.international_transportation_input_solar_cell[Supplier, port, transportation_type]
               for port in model.port for transportation_type in model.transportation_type)


def National_Transport_In_cell(model, port):
    """The amount of cell transport from potential_manufacturer to the manufacturer should be equal to the amount of cell received at the
     potential_manufacturer"""
    return sum(model.international_transportation_input_solar_cell[Supplier, port, transportation_type]
               for Supplier in model.Supplier for transportation_type in model.transportation_type) >= \
           sum(model.national_transportation_input_solar_cell[port, potential_manufacturer, transportation_type]
               for potential_manufacturer in model.potential_manufacturer for transportation_type in
               model.transportation_type)


def International_Transport_In_eva(model, Supplier):
    """The amount of purchased eva should be equal to amount eva transport to the potential_manufacturer"""
    return sum(model.purchasing_solar_eva[Supplier, month] for month in model.month) >= \
           sum(model.international_transportation_input_solar_eva[Supplier, port, transportation_type]
               for port in model.port for transportation_type in model.transportation_type)


def National_Transport_In_eva(model, port):
    """The amount of eva transport from potential_manufacturer to the manufacturer should be equal to the amount of eva received at the
     potential_manufacturer"""
    return sum(model.international_transportation_input_solar_eva[Supplier, port, transportation_type]
               for Supplier in model.Supplier for transportation_type in model.transportation_type) >= \
           sum(model.national_transportation_input_solar_eva[port, potential_manufacturer, transportation_type]
               for potential_manufacturer in model.potential_manufacturer for transportation_type in
               model.transportation_type)


def International_Transport_In_Al(model, Supplier):
    """The amount of purchased Al should be equal to amount Al transport to the potential_manufacturer"""
    return sum(model.purchasing_solar_Al[Supplier, month] for month in model.month) >= \
           sum(model.international_transportation_input_solar_Al[Supplier, port, transportation_type]
               for port in model.port for transportation_type in model.transportation_type)


def National_Transport_In_Al(model, port):
    """The amount of Al transport from potential_manufacturer to the manufacturer should be equal to the amount of Al received at the
     potential_manufacturer"""
    return sum(model.international_transportation_input_solar_Al[Supplier, port, transportation_type]
               for Supplier in model.Supplier for transportation_type in model.transportation_type) >= \
           sum(model.national_transportation_input_solar_Al[port, potential_manufacturer, transportation_type]
               for potential_manufacturer in model.potential_manufacturer for transportation_type in
               model.transportation_type)


def International_Transport_In_glass(model, Supplier):
    """The amount of purchased glass should be equal to amount glass transport to the potential_manufacturer"""
    return sum(model.purchasing_solar_glass[Supplier, month] for month in model.month) >= \
           sum(model.international_transportation_input_solar_glass[Supplier, port, transportation_type]
               for port in model.port for transportation_type in model.transportation_type)


def National_Transport_In_glass(model, port):
    """The amount of glass transport from potential_manufacturer to the manufacturer should be equal to the amount of glass received at
    the potential_manufacturer"""
    return sum(model.international_transportation_input_solar_glass[Supplier, port, transportation_type]
               for Supplier in model.Supplier for transportation_type in model.transportation_type) >= \
           sum(model.national_transportation_input_solar_glass[port, potential_manufacturer, transportation_type]
               for potential_manufacturer in model.potential_manufacturer for transportation_type in
               model.transportation_type)



def International_Transport_In_jBox(model, Supplier):
    """The amount of purchased jBox should be equal to amount jBox transport to the potential_manufacturer"""
    return sum(model.purchasing_solar_jBox[Supplier, month] for month in model.month) >= \
           sum(model.international_transportation_input_solar_jBox[Supplier, port, transportation_type]
               for port in model.port for transportation_type in model.transportation_type)


def National_Transport_In_jBox(model, port):
    """The amount of jBox transport from potential_manufacturer to the manufacturer should be equal to the amount of jBox
    received at the potential_manufacturer"""
    return sum(model.international_transportation_input_solar_jBox[Supplier, port, transportation_type]
               for Supplier in model.Supplier for transportation_type in model.transportation_type) >= \
           sum(model.national_transportation_input_solar_jBox[port, potential_manufacturer, transportation_type]
               for potential_manufacturer in model.potential_manufacturer for transportation_type in
               model.transportation_type)


def International_Transport_In_SealantPottingTapeStickers(model, Supplier):
    """The amount of purchased SealantPottingTapeStickers should be equal to amount SealantPottingTapeStickers
    transport to the potential_manufacturer """
    return sum(model.purchasing_solar_SealantPottingTapeStickers[Supplier, month] for month in model.month) >= \
           sum(model.international_transportation_input_solar_SealantPottingTapeStickers
               [Supplier, port, transportation_type]
               for port in model.port for transportation_type in model.transportation_type)


def National_Transport_In_SealantPottingTapeStickers(model, port):
    """The amount of SealantPottingTapeStickers transport from potential_manufacturer to the manufacturer should be equal to the amount
    of SealantPottingTapeStickers received at the potential_manufacturer"""
    return sum \
               (model.international_transportation_input_solar_SealantPottingTapeStickers[
                    Supplier, port, transportation_type]
                for Supplier in model.Supplier for transportation_type in model.transportation_type) >= \
           sum(model.national_transportation_input_solar_SealantPottingTapeStickers
               [port, potential_manufacturer, transportation_type]
               for potential_manufacturer in model.potential_manufacturer for transportation_type in
               model.transportation_type)


def International_Transport_In_TabbingsStringingRibbons(model, Supplier):
    """The amount of purchased TabbingsStringingRibbons should be equal to amount TabbingsStringingRibbons transport
    to the potential_manufacturer """
    return sum(model.purchasing_solar_TabbingsStringingRibbons[Supplier, month] for month in model.month) >= \
           sum(model.international_transportation_input_solar_TabbingsStringingRibbons
               [Supplier, port, transportation_type]
               for port in model.port for transportation_type in model.transportation_type)


def National_Transport_In_TabbingsStringingRibbons(model, port):
    """The amount of TabbingsStringingRibbons transport from potential_manufacturer to the manufacturer should be equal to the amount of
    TabbingsStringingRibbons received at the potential_manufacturer"""
    return sum(model.international_transportation_input_solar_TabbingsStringingRibbons[
                   Supplier, port, transportation_type]
               for Supplier in model.Supplier for transportation_type in model.transportation_type) >= \
           sum(model.national_transportation_input_solar_TabbingsStringingRibbons
               [port, potential_manufacturer, transportation_type]
               for potential_manufacturer in model.potential_manufacturer for transportation_type in
               model.transportation_type)


def Production_Capacity(model, potential_manufacturer):
    """This function still need more work. Wondering how to connect the potential_manufacturer to the final market"""
    return ((model.solar_module_production[potential_manufacturer]) * 545) <= \
           ((model.production_capacity[potential_manufacturer]) * model.module_center[potential_manufacturer])


def Production_binary(model):
    """Potential manufacturer candidate selection"""
    return sum(model.module_center[potential_manufacturer] for
               potential_manufacturer in model.potential_manufacturer) == Number_of_manufacturer


def Production_Out(model, potential_manufacturer):
    """The produced module should transport to national market or either international market"""
    return (model.solar_module_production[potential_manufacturer]) >= \
           (sum(model.national_transportation_out_solar_module[
                    potential_manufacturer, national_market, transportation_type]
                for national_market in model.national_market for transportation_type in model.transportation_type) +
            sum(model.international_transportation_out_solar_module[potential_manufacturer, port, transportation_type]
                for port in model.port for transportation_type in model.transportation_type))


def Module_Production_Cell(model, potential_manufacturer):
    return (model.solar_module_production[potential_manufacturer]) == \
           ((sum(model.national_transportation_input_solar_cell[port, potential_manufacturer, transportation_type]
                 for port in model.port for transportation_type in model.transportation_type)) / 72)


def Module_Production_Al(model, potential_manufacturer):
    return (model.solar_module_production[potential_manufacturer]) == \
           ((sum(model.national_transportation_input_solar_Al[port, potential_manufacturer, transportation_type]
                 for port in model.port for transportation_type in model.transportation_type)) / np.random.uniform(3.744, 4.755))


def Module_Production_eva(model, potential_manufacturer):
    return (model.solar_module_production[potential_manufacturer]) == \
           ((sum(model.national_transportation_input_solar_eva[port, potential_manufacturer, transportation_type]
                 for port in model.port for transportation_type in model.transportation_type)) / (2 * 2.583))


def Module_Production_glass(model, potential_manufacturer):
    return (model.solar_module_production[potential_manufacturer]) == \
           ((sum(model.national_transportation_input_solar_glass[port, potential_manufacturer, transportation_type]
                 for port in model.port for transportation_type in model.transportation_type)) / (2 * 2.583))


def Module_Production_jBox(model, potential_manufacturer):
    return (model.solar_module_production[potential_manufacturer]) == \
           ((sum(model.national_transportation_input_solar_jBox[port, potential_manufacturer, transportation_type]
                 for port in model.port for transportation_type in model.transportation_type)))


def Module_Production_SealantPottingTapeStickers(model, potential_manufacturer):
    return (model.solar_module_production[potential_manufacturer]) == \
           ((sum(model.national_transportation_input_solar_SealantPottingTapeStickers[port, potential_manufacturer,
                                                                                      transportation_type]
                 for port in model.port for transportation_type in model.transportation_type)))


def Module_Production_TabbingsStringingRibbons(model, potential_manufacturer):
    return (model.solar_module_production[potential_manufacturer]) == \
           ((sum(model.national_transportation_input_solar_TabbingsStringingRibbons[port, potential_manufacturer,
                                                                                    transportation_type]
                 for port in model.port for transportation_type in model.transportation_type)))

def Local_Demand_by_Production(model, national_market):
    """The amount of produced module should be equal to national demand. Since the demand unit is W, the module should
    multiply by 545. Each module output is considered to be 545"""
    return \
        ((sum(model.national_transportation_out_solar_module
              [potential_manufacturer, national_market, transportation_type] for potential_manufacturer in
              model.potential_manufacturer for transportation_type in model.transportation_type)) * 545) >= \
        (model.national_demand[national_market])


def Local_Demand_by_Import(model, national_market):
    """The amount of imported module should be equal to national demand. Since the demand unit is W, the module should
    multiply by 545. Each module output is considered to be 545W"""
    return ((sum(model.national_transportation_input_solar_module[port, national_market, transportation_type]
                 for port in model.port for transportation_type in model.transportation_type)) * 545) >= \
           (model.national_demand[national_market])


