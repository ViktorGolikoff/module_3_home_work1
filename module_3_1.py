calls = 0

def count_calls ():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    tuple_1 = ()
    display = len(string), string.upper(), string.lower()
    tuple_1 += display
    return tuple_1

def is_contains (string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower() == i.lower():
            return True
    return False

print(string_info("Felix"))
print(string_info("Melissa_Is_My_Cat"))
print(is_contains("Felix", ["Fel","Alix","Felixis","FelIX"]))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(f"Количество вызовов функций: {calls}")



