#Пошук даних за ПІБ
def search_person_data(dictionary):
    name = input("Введіть ПІБ: ") 
    if name in dictionary:
        print("\nДані про особу:")
        for k, v in dictionary[name].items():
            print(f"{k:<25}: {v}")
    else:
        print("Особа не знайдена.")



# Пошук за полем
def search_by_field(dictionary):

    selector = {
        1: "Hомер справи",
        2: "Дата відкриття справи",
        3: "Bік",
        4: "Вага",
        5: "Зріст"
        }
    
    print("\nПошук за полем:")
    for k, v in selector.items():
        print(f"{k}. {v}")

    try:
        key_selector = int(input("Оберіть номер поля: "))
        while key_selector not in selector:
            key_selector=int(input("Спробуйте ще раз: "))
        search_field = selector[key_selector]
    except ValueError:
        print("Неправильний вибір.")
        return
 
    value = input(f"Введіть значення для пошуку: ")
    if search_field in {"Bік", "Вага", "Зріст"}:
        try:
            value = int(value)
        except ValueError:
            print("Значення має бути числом")
            return

    # Шукаємо ключ за значенням
    keyFromValue = [key for key, details in dictionary.items() if details.get(search_field) == value]
#keyFromValue = []  
#for key, details in dictionary.items(): 
#   if search_field in details:  # чи є таке поле
#       if details[search_field] == value: 
#           keyFromValue.append(key)  
    if keyFromValue:
        print("\nЗнайдені особи:")
        for result in keyFromValue:
            print(result)
    else:
        print("За даним критерієм пошуку нічого не знайдено.")
