import InterestRate as ir
import CompoundingFrequency as cfr
import DiscountFactor as df
import PresentValue as pv

ir.comp_to_cont(0.08, cfr.semi_annually())

years = [0.5,1,1.5,2]
cash_flows = [80, 120, 160, 1200]
disc_factors = []
for year in years:
    disc_factors.append(df.disc_factor(r=0.08,m=cfr.semi_annually(), t=year))

present_values = []
for i in range(len(cash_flows)):
    present_values.append(pv.present_value(cash_flows[i],disc_factors[i]))