from pyomo.environ import *
from Joule_database_AU import *

class SolarModel(ConcreteModel):
    def __init__(self, i, t):
        super().__init__()

        self.Supplier = Set(initialize=Suppliers_Set("Suppliers_Name"))
        self.potential_manufacturer = Set(initialize=Manufacturer_Set("Location_Name"))
        self.national_market = Set(initialize=National_Market_Set("National_Market_Name"))
        self.international_market = Set(initialize=International_Market_Set("International_Market_Name"))
        self.month = Set(initialize=Suppliers_Set("Month"))
        self.transportation_type = Set(initialize=International_Transportation_In_Set("Type"))
        self.port = Set(initialize=International_Transportation_In_Set("Location_Port_Name"))
        self.product = Set(initialize=Suppliers_Set("Product"))

        # Placeholder for additional model-specific initialization code


def create_solar_model(i, t):
    return SolarModel(i, t)

