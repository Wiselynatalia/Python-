#python_version == '3.7.4'
def recursive_sqrt(a, x):
    value = (1/2)*(x + (a/x))
    if abs(value - x) <= 0.001:
        return value
    else:
        return recursive_sqrt(a, value)
