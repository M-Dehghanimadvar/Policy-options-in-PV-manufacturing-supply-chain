# Quantifying the Costs of Diversifying Silicon PV Module Assembly with Local Economic Policies

This code quantifies the cost of local economic policies on the supply chain of Si PV module manufacturing. The proposed model, first optimized the MSP and then the price gaps between locally assembled and imported PV modules. Then assess the required policy to cover the price gap. Two types of policies are assessed, supportive and protective policies. 

### Protective policies:

- Equipment incentives: the government pays a % of equipment CapEx
- Facility incentives: the government pays % of land/building CapEx
- Labour incentives: the government pays % of direct labour expenses for the first year of factory operation
- Electricity incentives: the government pays % of electricity expenses over 7 years of factory operation.
- Tax incentives: the government gives an exemption of % of the corporate tax
- Free-interest loan: the government gives a free-interest loan for a % of total borrowing for 7 years of factory operation (Note: debt-to-equity ratio for this incentive is assumed to be 50%) 

### Supportive policies:
- Import tariffs
- Import quota
- Import embargo


# Requirements
Python package dependent
  - json
  - os
  - time
  - pandas
  - numpy
  - numpy_financial
  - pyomo


# Dataset
The excel file is provided as a data source for input data. All required data can be updated according to the considered technology. For instance, required data for 72 cells bifacial mono-crystalline PERC is upload as per candidate locations (Australia, Germany, USA) datasets as Excel files. For any uncertain data, a uniform distribution is used. A Monte Carlo analysis is then conducted to address any uncertatinties within the datasets.


