def calculate_structure_sum(data_structure):
    numb = 0
    if isinstance(data_structure, list):
        for i in data_structure:
            numb += calculate_structure_sum(i)

    elif isinstance(data_structure, tuple):
        for x in data_structure:
            numb += calculate_structure_sum(x)

    elif isinstance(data_structure, set):
        for y in data_structure:
            numb += calculate_structure_sum(y)

    elif isinstance(data_structure, dict):
        for k, v in data_structure.items():
            numb += calculate_structure_sum(k) + calculate_structure_sum(v)

    elif isinstance(data_structure, str):
        return len(data_structure)

    elif data_structure is None:
        return 0

    else:
        return data_structure

    return numb


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)







#     length = 0
#
#     for key, value in data_structure.items():
#         length += len(str(key))
#         if isinstance(value, dict):
#             length += calculate_structure_sum(value)
#         else:
#             length += len(str(value))
#     return length
#
# print(calculate_structure_sum(data_structure))
    # a = data_structure[0]
    # b = data_structure[1]
    # c = data_structure[2]
    # d = data_structure[3]
    # e = data_structure[4]
    # if isinstance(data_structure, int):
    #     a = sum(data_structure)
    # if isinstance(data_structure, str):
    #     b = sum(len(str(data_structure)))
    # result = a + b


    #     for key,value in data_structure.items():
    #         sum(len(str(key)) + sum(value)
    # elif


# result = calculate_structure_sum(data_structure)
# print(result)