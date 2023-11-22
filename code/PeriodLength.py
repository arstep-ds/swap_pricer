def period_length(t1,t2):
    if t2 <= t1:
        raise ValueError("t2 must be larger than t1")
    else:
        return t2-t1

# working with data
def period_length_data(years):
    pl = []
    if years[0] == 0:
        pl.append(years[1])
    else:
        pl.append(years[0])

    for i in range(len(years)-1):
        pl.append(period_length(t1=years[i], t2=years[i+1]))
    
    return pl