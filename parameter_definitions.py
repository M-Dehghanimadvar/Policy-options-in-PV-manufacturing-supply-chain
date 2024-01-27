from pyomo.environ import *
from Joule_database_AU import *

from pyomo.environ import *


class ParameterDefinitions:
    def __init__(self, model, Cap):
        self.model = model
        self.model.solar_module_purchasing_cost = Param(self.model.Supplier, self.model.month,
                                                        initialize=lambda model, suppliers, month:
                                                        Param_Suppliers(model, "Price", "Module", None, suppliers,
                                                                        month))
        self.model.solar_cell_purchasing_cost = Param(self.model.Supplier, self.model.month,
                                                      initialize=lambda model, suppliers, month:
                                                      Param_Suppliers(model, "Price", "Cell", Cap, suppliers,
                                                                      month))

        self.model.fixed_cost_module_center = \
            Param(self.model.potential_manufacturer,
                  initialize=(np.random.uniform(0.012, 0.05) * (
                          (Cap / 1000000000) ** -(np.random.uniform(0.05, 0.015)))) * Cap)
        self.model.production_capacity = Param(self.model.potential_manufacturer,
                                          initialize=Cap + 1000)

        self.model.international_transportation_input_cost_cell = \
            Param(self.model.Supplier, self.model.port, self.model.transportation_type,
                  initialize=lambda model, suppliers, port, type:
                  Param_International_Transportation_In(model, "Price", "Cell", suppliers, port, type))

        self.model.international_transportation_input_cost_eva = \
            Param(self.model.Supplier, self.model.port, self.model.transportation_type,
                  initialize=lambda model, suppliers, port, type:
                  Param_International_Transportation_In(model, "Price", "EVA", suppliers, port, type))

        self.model.international_transportation_input_cost_glass = \
            Param(self.model.Supplier, self.model.port, self.model.transportation_type,
                  initialize=lambda model, suppliers, port, type:
                  Param_International_Transportation_In(model, "Price", "Glass", suppliers, port, type))

        self.model.international_transportation_input_cost_Al = \
            Param(self.model.Supplier, self.model.port, self.model.transportation_type,
                  initialize=lambda model, suppliers, port, type:
                  Param_International_Transportation_In(model, "Price", "Aluminium", suppliers, port, type))

        self.model.international_transportation_input_cost_jBox = \
            Param(self.model.Supplier, self.model.port, self.model.transportation_type,
                  initialize=lambda model, suppliers, port, type:
                  Param_International_Transportation_In(model, "Price", "JunctionBox", suppliers, port, type))

        self.model.international_transportation_input_cost_TabbingsStringingRibbons = \
            Param(self.model.Supplier, self.model.port, self.model.transportation_type,
                  initialize=lambda model, suppliers, port, type:
                  Param_International_Transportation_In(model, "Price", "TabbingsStringingRibbons", suppliers, port,
                                                        type))

        self.model.international_transportation_input_cost_SealantPottingTapeStickers = \
            Param(self.model.Supplier, self.model.port, self.model.transportation_type,
                  initialize=lambda model, suppliers, port, type:
                  Param_International_Transportation_In(model, "Price", "SealantPottingTapeStickers", suppliers, port,
                                                        type))

        self.model.national_transportation_input_cost_cell = \
            Param(self.model.port, self.model.potential_manufacturer, self.model.transportation_type,
                  initialize=lambda model, port, potential_manufacturer, type:
                  Param_National_Transportation_In(model, "Price", "Cell", port, potential_manufacturer, type))

        self.model.national_transportation_input_cost_Al = \
            Param(self.model.port, self.model.potential_manufacturer, self.model.transportation_type,
                  initialize=lambda model, port, potential_manufacturer, type:
                  Param_National_Transportation_In(model, "Price", "Aluminium", port, potential_manufacturer, type))

        self.model.national_transportation_input_cost_eva = \
            Param(self.model.port, self.model.potential_manufacturer, self.model.transportation_type,
                  initialize=lambda model, port, potential_manufacturer, type:
                  Param_National_Transportation_In(model, "Price", "EVA", port, potential_manufacturer, type))

        self.model.national_transportation_input_cost_glass = \
            Param(self.model.port, self.model.potential_manufacturer, self.model.transportation_type,
                  initialize=lambda model, port, potential_manufacturer, type:
                  Param_National_Transportation_In(model, "Price", "Glass", port, potential_manufacturer, type))

        self.model.national_transportation_input_cost_jBox = \
            Param(self.model.port, self.model.potential_manufacturer, self.model.transportation_type,
                  initialize=lambda model, port, potential_manufacturer, type:
                  Param_National_Transportation_In(model, "Price", "JunctionBox", port, potential_manufacturer, type))

        self.model.national_transportation_input_cost_TabbingsStringingRibbons = \
            Param(self.model.port, self.model.potential_manufacturer, self.model.transportation_type,
                  initialize=lambda model, port, potential_manufacturer, type:
                  Param_National_Transportation_In(model, "Price", "TabbingsStringingRibbons", port, potential_manufacturer, type))

        self.model.national_transportation_input_cost_SealantPottingTapeStickers = \
            Param(self.model.port, self.model.potential_manufacturer, self.model.transportation_type,
                  initialize=lambda model, port, potential_manufacturer, type:
                  Param_National_Transportation_In(model, "Price", "SealantPottingTapeStickers", port, potential_manufacturer, type))

        self.model.national_transportation_out_cost_solar_module = \
            Param(self.model.potential_manufacturer, self.model.national_market, self.model.transportation_type,
                  initialize=0.00000002)
        self.model.international_transportation_input_cost_module = \
            Param(self.model.Supplier, self.model.port, self.model.transportation_type,
                  initialize=0.00000002)
        self.model.national_transportation_input_cost_module = \
            Param(self.model.port, self.model.national_market, self.model.transportation_type,
                  initialize=0.00000002)


        self.model.solar_module_capacity = Param(self.model.Supplier, self.model.month,
                                            initialize=Cap+1000000)

        self.model.solar_cell_capacity = Param(self.model.Supplier, self.model.month,
                                          initialize=Cap+1000000)

        self.model.solar_Al_capacity = Param(self.model.Supplier, self.model.month,
                                        initialize=Cap+1000000)

        self.model.solar_glass_capacity = Param(self.model.Supplier, self.model.month,
                                           initialize=Cap+1000000)

        self.model.solar_eva_capacity = Param(self.model.Supplier, self.model.month,
                                         initialize=Cap+1000000)

        self.model.solar_JBox_capacity = Param(self.model.Supplier, self.model.month,
                                          initialize=Cap+1000000)

        self.model.solar_TabbingsStringingRibbons_capacity = Param(self.model.Supplier, self.model.month,
                                                              initialize=Cap+1000000)

        self.model.solar_SealantPottingTapeStickers_capacity = Param(self.model.Supplier, self.model.month,
                                                                initialize=Cap+1000000)


        self.model.import_tariff_module = Param(
            initialize=0)
        self.model.import_tariff_BoMs = Param(initialize=0)

        self.model.solar_Al_purchasing_cost = Param(self.model.Supplier, self.model.month,
                                               initialize=lambda model, suppliers, month:
                                               Param_Suppliers(model, "Price", "Aluminium", Cap, suppliers, month))

        self.model.solar_glass_purchasing_cost = Param(self.model.Supplier, self.model.month,
                                                  initialize=lambda model, suppliers, month:
                                                  Param_Suppliers(model, "Price", "Glass", Cap, suppliers, month))

        self.model.solar_eva_purchasing_cost = Param(self.model.Supplier, self.model.month,
                                                initialize=lambda model, suppliers, month:
                                                Param_Suppliers(model, "Price", "EVA", Cap, suppliers, month, ))

        self. model.solar_jBox_purchasing_cost = Param(self.model.Supplier, self.model.month,
                                                 initialize=lambda model, suppliers, month:
                                                 Param_Suppliers(model, "Price", "JunctionBox", Cap, suppliers, month))

        self.model.solar_TabbingsStringingRibbons_purchasing_cost = Param(self.model.Supplier, self.model.month,
                                                                     initialize=lambda model, suppliers, month:
                                                                     Param_Suppliers(model, "Price",
                                                                                     "TabbingsStringingRibbons", Cap,
                                                                                     suppliers,
                                                                                     month))

        self.model.solar_SealantPottingTapeStickers_purchasing_cost = Param(self.model.Supplier, self.model.month,
                                                                       initialize=lambda model, suppliers, month:
                                                                       Param_Suppliers(model, "Price",
                                                                                       "SealantPottingTapeStickers",
                                                                                       Cap,
                                                                                       suppliers, month))

        self.model.labour_cost = Param(self.model.potential_manufacturer,
                                  initialize=lambda model, potential_manufacturer:
                                  Param_Potential_Manufacturer(model, "LabourCost", Cap, potential_manufacturer))

        self.model.electricity_cost = Param(self.model.potential_manufacturer,
                                       initialize=lambda model, potential_manufacturer:
                                       Param_Potential_Manufacturer(model, "ElectricityCost", Cap,
                                                                    potential_manufacturer))


        # Placeholder for additional model-specific initialization code
