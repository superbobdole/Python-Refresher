def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
# map can do the same thing as this list comprehension
# list comprehension is faster
doubled = map(double, sequence)
# lambda style
doubled = map(lambda x: x * 2, sequence)
# to print
doubled = list(map(lambda x: x * 2, sequence))
