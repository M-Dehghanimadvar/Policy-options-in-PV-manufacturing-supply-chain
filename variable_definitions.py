from pyomo.environ import *


class VariableDefinitions:
    def __init__(self, model):
        self.model = model

        # Define your variables here
        self.model.module_center = Var(self.model.potential_manufacturer, within=Binary)

        self.model.purchasing_solar_module = Var(self.model.Supplier, self.model.month, within=NonNegativeIntegers)
        self.model.purchasing_solar_cell = Var(self.model.Supplier, self.model.month, within=NonNegativeIntegers)
        self.model.purchasing_solar_eva = Var(self.model.Supplier, self.model.month, within=NonNegativeIntegers)
        self.model.purchasing_solar_glass = Var(self.model.Supplier, self.model.month, within=NonNegativeReals)
        self.model.purchasing_solar_Al = Var(self.model.Supplier, self.model.month, within=NonNegativeReals)
        self.model.purchasing_solar_jBox = Var(self.model.Supplier, self.model.month, within=NonNegativeReals)
        self.model.purchasing_solar_SealantPottingTapeStickers = Var(self.model.Supplier, self.model.month, within=NonNegativeReals)
        self.model.purchasing_solar_TabbingsStringingRibbons = Var(self.model.Supplier, self.model.month, within=NonNegativeReals)

        self.model.international_transportation_input_solar_module = Var(self.model.Supplier, self.model.port,
                                                                        model.transportation_type,
                                                                        within=NonNegativeIntegers)

        self.model.international_transportation_input_solar_cell = Var(self.model.Supplier, self.model.port, self.model.transportation_type,
                                                                      within=NonNegativeIntegers)
        self.model.international_transportation_input_solar_eva = Var(self.model.Supplier, self.model.port, self.model.transportation_type,
                                                                     within=NonNegativeReals)
        self.model.international_transportation_input_solar_glass = Var(self.model.Supplier, self.model.port,
                                                                       self.model.transportation_type,
                                                                       within=NonNegativeReals)
        self.model.international_transportation_input_solar_Al = Var(self.model.Supplier, self.model.port, self.model.transportation_type,
                                                                    within=NonNegativeReals)
        self.model.international_transportation_input_solar_jBox = Var(self.model.Supplier, self.model.port, self.model.transportation_type,
                                                                      within=NonNegativeReals)
        self.model.international_transportation_input_solar_SealantPottingTapeStickers = \
            Var(self.model.Supplier, self.model.port, self.model.transportation_type, within=NonNegativeReals)
        self.model.international_transportation_input_solar_TabbingsStringingRibbons = \
            Var(self.model.Supplier, self.model.port, self.model.transportation_type, within=NonNegativeReals)

        self.model.national_transportation_input_solar_module = \
            Var(self.model.port, self.model.national_market, self.model.transportation_type, within=NonNegativeIntegers)
        self.model.national_transportation_out_solar_module = \
            Var(self.model.potential_manufacturer, self.model.national_market, self.model.transportation_type,
                within=NonNegativeIntegers)
        self.model.international_transportation_out_solar_module = \
            Var(self.model.potential_manufacturer, self.model.port, self.model.transportation_type, within=NonNegativeIntegers)
        self.model.national_transportation_input_solar_cell = \
            Var(self.model.port, self.model.potential_manufacturer, self.model.transportation_type, within=NonNegativeIntegers)
        self.model.national_transportation_input_solar_eva = \
            Var(self.model.port, self.model.potential_manufacturer, self.model.transportation_type, within=NonNegativeReals)
        self.model.national_transportation_input_solar_glass = \
            Var(self.model.port, self.model.potential_manufacturer, self.model.transportation_type, within=NonNegativeReals)
        self.model.national_transportation_input_solar_Al = \
            Var(self.model.port, self.model.potential_manufacturer, self.model.transportation_type, within=NonNegativeReals)
        self.model.national_transportation_input_solar_jBox = \
            Var(self.model.port, self.model.potential_manufacturer, self.model.transportation_type, within=NonNegativeReals)
        self.model.national_transportation_input_solar_SealantPottingTapeStickers = \
            Var(self.model.port, self.model.potential_manufacturer, self.model.transportation_type, within=NonNegativeReals)
        self.model.national_transportation_input_solar_TabbingsStringingRibbons = \
            Var(self.model.port, self.model.potential_manufacturer, self.model.transportation_type, within=NonNegativeReals)

        self.model.solar_module_production = Var(self.model.potential_manufacturer, within=NonNegativeIntegers)
