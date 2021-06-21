def quadratic_formula(a,b,c):
    y = []
    x1 = (-b+(b**2-4*a*c)**.5)/2*a
    x2 = (-b-(b**2-4*a*c)**.5)/2*a
    if a*x1**2+b*x1+c == 0:
        y.append(x1)
    if a*x2**2+b*x2+c == 0:
        y.append(x2)
    if len(y) == 0:
        return None
    else:
        return tuple(set(y))
