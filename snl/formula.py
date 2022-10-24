def pv(type, fv, i, t):
    pv=0
    if type == "lump-sum":
        pv = fv/(1+i)**t
    else:
        pv = fv*i/((1+i)**t-1)
    return round(pv,2)

def fv(type,pv, i, t):
    fv=0
    if type == "lump-sum":
        fv = pv*((1+i)**t)
    else:
        fv = (pv/i)*((1+i)**t)
    return round(fv,2)