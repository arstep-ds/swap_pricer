import math

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