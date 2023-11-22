import math
import DiscountFactor as df
import PeriodLength as pl
import InterestRate as ir

def implied_forwards_simple(r_T1, T1, r_T2, T2):
    """Implied forward with simple rates r_T1 and r_T2,
    and time points in years T1 and T2, where T2 > T1"""
    T = T2-T1
    r_tT = (1/T) * (((1+r_T2*T2)/(1+r_T1*T1))-1)
    return r_tT

def implied_forwards_comp(r_T1, T1, r_T2, T2, m):
    """Implied forward with compunding rates r_T1 and r_T2,
    and time points in years T1 and T2, where T2 > T1, and
    compunding frequency m"""
    T = T2-T1
    up = (1+r_T2/m)**(m*T2)
    dn = (1+r_T1/m)**(m*T1)
    r_tT = m * (((up/dn)**(1/(m*T))) -1)
    return r_tT

def implied_forwards_cont(r_T1, T1, r_T2, T2):
    """Implied forward with countinuous rates r_T1 and r_T2,
    and time points in years T1 and T2, where T2 > T1"""
    return (r_T2*T2 - r_T1*T1) / (T2-T1)

def implied_forwards_discfactor_comp(df_T1, df_T2, T1, T2, m):
    """Implied forward with compunding discount factors df_T1 and df_T2,
    and time points in years T1 and T2, where T2 > T1, and
    compunding frequency m"""
    T = T2 - T1
    df_tT = df_T2 / df_T1
    return m * ((df_tT ** (-1/m*T))-1)

def implied_forwards_discfactor_simple(df_T1, df_T2, T1, T2):
    """Implied forward with simple discount factors df_T1 and df_T2,
    and time points in years T1 and T2, where T2 > T1"""
    T = T2 - T1
    df_tT = df_T2 / df_T1
    return (1/T) * ((df_tT**-1)-1)

def implied_forwards_discfactor_cont(df_T1, df_T2, T1, T2):
    """Implied forward with continuous discount factors df_T1 and df_T2,
    and time points in years T1 and T2, where T2 > T1"""
    return (-1/(T2-T1)) * math.log(df_T2 / df_T1)

# working with data
def impl_fwd_swap(rates, years):
    period_length = pl.period_length_data(years)
    disc_factors = []
    for i in range(len(rates)):
        disc_factors.append(df.disc_factor_cont_rate(rates[i],t=years[i]))

    implied_forwards = []
    implied_forwards.append(rates[0])
    for i in range(len(rates)-1):
        implied_forwards.append(implied_forwards_discfactor_cont(df_T1=disc_factors[i], df_T2=disc_factors[i+1], T1=years[i], T2=years[i+1]))

    implied_forwards_simple = []
    for i in range(len(rates)):
        implied_forwards_simple.append(ir.cont_to_simple(implied_forwards[i],period_length[i]))
    
    return implied_forwards_simple