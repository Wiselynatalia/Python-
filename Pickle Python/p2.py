#python_version == '3.7.4'
def quicksort(a):
    if len(a) == 0:
        return ([])
    else:
        pivot = a[0]
        lhs = quicksort([i for i in a[1:] if i > pivot])
        rhs = quicksort([i for i in a[1:] if i <= pivot])
    return (lhs+[pivot]+rhs)

