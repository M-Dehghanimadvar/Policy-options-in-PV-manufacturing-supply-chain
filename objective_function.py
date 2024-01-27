from pyomo.environ import *
from Functions import *

class ObjectiveDefinition:
    def __init__(self, model):
        self.model = model
        self.model.Objective_function = Objective(rule=Objective_Function, sense=minimize)
