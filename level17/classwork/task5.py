data = [1, 2, 3, True, False, "hello", "python"]

integer = []
bool_list = []
string = []

for item in data:
    if type(item) == int:
        integer.append(item)
    elif type(item) == bool:
        bool_list.append(item)
    elif type(item) == str:
        string.append(item)

integer = tuple(integer)
bool_list = tuple(bool_list)
string = tuple(string)

print(integer)
print(bool_list)
print(string)