#python_version == '3.7.4'
a = [i for i in range(1,11)]
cubic = list(map(lambda x : x**3, a))
add_one = list(map(lambda x: x+1, a))
less_than_or_equal_to_5 = [i for i in a if i<=5]
square_of_odd_values = [i**2 for i in a if i%2 != 0 ]
