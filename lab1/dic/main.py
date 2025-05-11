from dic_data_module import create_dictionary
from search_module import search_by_field, search_person_data
from modify_module import modify_data

dic = create_dictionary()#осн. словник

search_person_data(dic)#Пошук даних за ПІБ
search_by_field(dic)#Пошук за полем
modify_data(dic)

print("\nОновлена база даних:")
for name, info in dic.items():
    print(f"\n{name}:")
    for k, v in info.items():
        print(f"  {k:<25}: {v}")



