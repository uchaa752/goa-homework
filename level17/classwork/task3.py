numbers = set()

numbers.add(10)
numbers.add(5)
numbers.add(20)

numbers_tuple = tuple(numbers)

print(numbers_tuple)

print(max(numbers_tuple))
print(min(numbers_tuple))

print(max(numbers_tuple) + min(numbers_tuple))