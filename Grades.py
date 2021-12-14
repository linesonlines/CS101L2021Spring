import math

def total(list_vals):
    return float(sum(list_vals))

def average(list_vals):
    if len(list_vals) == 0:
        return math.nan
    else:
        return float(sum(list_vals) / len(list_vals))

def median(list_vals):
    list_vals.sort()
    length = len(list_vals)
    if length == 1:
        return list_vals[0]
    elif length == 0:
        raise ValueError
        #pass
    else:
        isEven = (length % 2 == 0)
        if isEven:
            index1 = int(length / 2) - 1
            index2 = int(length / 2)
            median = (list_vals[index1] + list_vals[index2]) / 2
            return median
        else:
            index = math.floor(length / 2)
            median = list_vals[index]
            return median
