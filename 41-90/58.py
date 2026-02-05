def my_map (func, iterable):
    result = []
    for item in iterable:
        processed_item = func(item)
        result.append(processed_item)
    return result

def square(x):
    return x ** 2

def to_upper(s):
    return s.upper()

numbers = [1, 2, 3, 4, 5]
squared_numbers = my_map(square, numbers)
print(squared_numbers)

strings = ['hello', 'world', 'python']
upper_strings = my_map(to_upper, strings)
print(upper_strings)