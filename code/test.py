import ImpliedForward as ifwd
import InterestRate as ir
import DiscountFactor as df

years = [0.49589, 1, 1.49589, 2]
rates = [0.0089, 0.0123, 0.0141, 0.0163]
period_length = [0.49589, 0.50411, 0.49589, 0.50411]

disc_factors = []
for i in range(4):
    disc_factors.append(df.disc_factor_cont_rate(rates[i],t=years[i]))

implied_forwards = []
implied_forwards.append(ir.cont_to_simple(r_c=rates[0],t=years[0]))
for i in range(3):
    implied_forwards.append(ifwd.implied_forwards_discfactor_cont(df_T1=disc_factors[i], df_T2=disc_factors[i+1], T1=years[i], T2=years[i+1]))

implied_forwards_simple = []
implied_forwards_simple.append(implied_forwards[0])
for i in range(3):
    implied_forwards_simple.append(ir.cont_to_simple(implied_forwards[i+1],period_length[i+1]))