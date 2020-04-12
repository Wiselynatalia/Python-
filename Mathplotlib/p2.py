#python_version == '3.7.4'
from functools import reduce
def word_count(x, str, n):
    string = list(filter(lambda y: len(y)>n,x))
    count = list(map(lambda x: x.count(str),string))
    return(reduce(lambda a,b: a+b, count))
    

