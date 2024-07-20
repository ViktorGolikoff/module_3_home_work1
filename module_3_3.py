#Exercise №1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()#работает
print_params(b = 25)#работает
print_params(c = [1, 2, 3])#работает
print_params(a = "Meow")#работает
print_params(a = 98 ,b = "Russia", c = False)#работает

#Exercise №2
values_list = ["Air", 5, False]
values_dict = {"a":"Air", "b":5, "c":False}
print_params(*value_list, **values_dict)
#Не получится передать список values_list и словарь values_dict в функцию print_paras
#поскольку функция имеет только три параметра, а не шесть.

#Exercise №3
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)#работает