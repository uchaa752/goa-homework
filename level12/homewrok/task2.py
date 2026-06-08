def minimum(numbers):
    min_num = numbers[0]

    for i in numbers:
        if i < min_num:
            min_num = i
    return min_num

print(minimum([4, 3, 2, 5, 7, 9]))