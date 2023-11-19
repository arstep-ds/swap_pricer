import InterestRate as ir
import CompoundingFrequency as cfr
import DiscountFactor as df

ir.comp_to_cont(0.06, cfr.semi_annually())

years = [0,0.5,1,1.5,2,2.5,3,4,5,6,7,8,9,10]

disc_factors = []
for year in years:
    disc_factors.append(df.disc_factor(r=0.1,m=cfr.semi_annually(), t=year))