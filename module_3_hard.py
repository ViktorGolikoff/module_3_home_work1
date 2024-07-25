def calculate_structure_sum(args):
    final_sum = 0
    for i in args:
        if isinstance(i, str):
            final_sum += len(i)
        if isinstance(i, int):
            final_sum += i
        if isinstance(i, list):
            final_sum += calculate_structure_sum(i)
        if isinstance(i, tuple):
            final_sum += calculate_structure_sum(i)
        if isinstance(i, dict):
            final_sum += calculate_structure_sum(i.items())
        if isinstance(i, set):
            final_sum += calculate_structure_sum(i)
    return final_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)