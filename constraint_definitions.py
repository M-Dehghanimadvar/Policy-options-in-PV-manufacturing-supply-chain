from pyomo.environ import *
from Functions import *

class ConstraintDefinitions:
    def __init__(self, model, Cap, Quota):
        self.model = model
        self.Production_Capacity_con = Constraint(model.potential_manufacturer, rule=Production_Capacity)

        self.model.national_demand = Param(model.national_market, initialize=Cap)

        self.model.International_Module_Capacity_con = \
            Constraint(model.Supplier, rule=lambda model, Supplier:
                       International_Module_Capacity(model, Supplier, Quota))

        self.model.International_cell_Capacity_con = \
            Constraint(model.Supplier, rule=lambda model, Supplier:
                       International_cell_Capacity(model, Supplier, Quota))

        self.model.International_Al_Capacity_con = \
            Constraint(model.Supplier, rule=lambda model, Supplier:
                       International_Al_Capacity(model, Supplier, Quota))

        self.model.International_Glass_Capacity_con = \
            Constraint(model.Supplier, rule=lambda model, Supplier:
                       International_Glass_Capacity(model, Supplier, Quota))

        self.model.International_EVA_Capacity_con = \
            Constraint(model.Supplier, rule=lambda model, Supplier:
                       International_EVA_Capacity(model, Supplier, Quota))

        self.model.International_JBox_Capacity_con = \
            Constraint(model.Supplier, rule=lambda model, Supplier:
                       International_JBox_Capacity(model, Supplier, Quota))

        self.model.International_TabbingsStringingRibbons_Capacity_con = \
            Constraint(model.Supplier, rule=lambda model, Supplier:
                       International_TabbingsStringingRibbons_Capacity(model, Supplier, Quota))

        self.model.International_SealantPottingTapeStickers_Capacity_con = \
            Constraint(model.Supplier, rule=lambda model, Supplier:
                       International_SealantPottingTapeStickers_Capacity(model, Supplier, Quota))

        self.model.International_Transport_In_Module_con = Constraint(model.Supplier, rule=International_Transport_In_Module)

        self.model.National_Transport_In_Module_con = Constraint(model.port, rule=National_Transport_In_Module)

        self.model.International_Transport_In_cell_con = Constraint(model.Supplier, rule=International_Transport_In_cell)

        self.model.National_Transport_In_cell_con = Constraint(model.port, rule=National_Transport_In_cell)

        self.model.International_Transport_In_eva_con = Constraint(model.Supplier, rule=International_Transport_In_eva)

        self.model.National_Transport_In_eva_con = Constraint(model.port, rule=National_Transport_In_eva)

        self.model.International_Transport_In_Al_con = Constraint(model.Supplier, rule=International_Transport_In_Al)

        self.model.National_Transport_In_Al_con = Constraint(model.port, rule=National_Transport_In_Al)

        self.model.International_Transport_In_glass_con = Constraint(model.Supplier, rule=International_Transport_In_glass)

        self.model.National_Transport_In_glass_con = Constraint(model.port, rule=National_Transport_In_glass)

        self.model.International_Transport_In_jBox_con = Constraint(model.Supplier, rule=International_Transport_In_jBox)

        self.model.National_Transport_In_jBox_con = Constraint(model.port, rule=National_Transport_In_jBox)

        self.model.International_Transport_In_SealantPottingTapeStickers_con = \
            Constraint(model.Supplier, rule=International_Transport_In_SealantPottingTapeStickers)

        self.model.National_Transport_In_SealantPottingTapeStickers_con = \
            Constraint(model.port, rule=National_Transport_In_SealantPottingTapeStickers)

        self.model.International_Transport_In_TabbingsStringingRibbons_con = \
            Constraint(model.Supplier, rule=International_Transport_In_TabbingsStringingRibbons)

        self.model.National_Transport_In_TabbingsStringingRibbons_con = \
            Constraint(model.port, rule=National_Transport_In_TabbingsStringingRibbons)

        self.model.Production_binary_con = Constraint(rule=Production_binary)
        self.model.Production_Out_con = Constraint(model.potential_manufacturer, rule=Production_Out)

        self.model.Module_Production_Cell = Constraint(model.potential_manufacturer, rule=Module_Production_Cell)

        self.model.Module_Production_Al = Constraint(model.potential_manufacturer, rule=Module_Production_Al)

        self.model.Module_Production_eva = Constraint(model.potential_manufacturer, rule=Module_Production_eva)

        self.model.Module_Production_glass = Constraint(model.potential_manufacturer, rule=Module_Production_glass)

        self.model.Module_Production_jBox = Constraint(model.potential_manufacturer, rule=Module_Production_jBox)

        self.model.Module_Production_SealantPottingTapeStickers = \
            Constraint(model.potential_manufacturer, rule=Module_Production_SealantPottingTapeStickers)

        self.model.Module_Production_TabbingsStringingRibbons = \
            Constraint(model.potential_manufacturer, rule=Module_Production_TabbingsStringingRibbons)

        self.Demand_Constraint("Local")

    def Demand_Constraint(self, mode):
        if mode == "Local":
            self.model.Local_Demand_by_Production_con = Constraint(self.model.national_market,
                                                                   rule=Local_Demand_by_Production)
            return
        if mode == "Global":
            self.model.Local_Demand_by_Import_con = Constraint(self.model.national_market,
                                                               rule=Local_Demand_by_Import)
            return
        return print("Error")
