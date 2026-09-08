def paob(a, b, apo):
    pa = len(a)/len(apo)
    pb = len(b)/len(apo)
    i = a.intersection(b)
    pi = len(i)/len(apo)
    return(pa + pb - pi)

e = {2,4,6}
g = {3,4,5,6}
apr = {1,2,3,4,5,6}
print('Probability of Getting an even number or a number greater than 2')
print(paob, g, apr )