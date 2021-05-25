#Gabriel and Zach
def average(ilist):
    sum = 0
    for element in ilist:
        sum+=element
    mean = (sum / len(ilist))
    return mean

def standardDeviation(ilist):
    mean = average(ilist)
    varsum = 0
    for element in ilist:
        varsum+= ((element - mean)**2)
    variance = (varsum / (len(ilist)))
    deviation = (variance**(1/2))
    return deviation

def median(ilist):
    ilist = sorted(ilist)
    if ((len(ilist) % 2) != 0):  #odd length
        median = (ilist[int((len(ilist)/2) - 0.5)])
    if ((len(ilist) % 2) == 0):  #even length
        lowMedian = (ilist[int((len(ilist)/2) - 0.5)])
        highMedian = (ilist[int((len(ilist)/2) + 0.5)])
        median = ((lowMedian + highMedian)/2)
    return median

L = [5,3,1,2,4]
print(average(L))
print(standardDeviation(L))
print(median(L))
