def get_categories(text, default_categories):
    selector = int(input(
        f"{text}:\n"
        "  Натисніть 1 — вибрати шаблон\n"
        "  Натисніть 2 — ввести власні категорії\n"
        "Ваш вибір: "))

    while selector not in [1,2]:
        selector=int(input("Некоректно. Спробуйте ще раз: "))

    if selector == 2:
        categories_number = int(input("Bведіть кількість категорій: "))
        categories=[]
        for categorie in range(categories_number):
            categorie = input(f"введіть категорію {categorie+1}: ")
            categories.append(categorie)
        return categories
    else:
        return default_categories

        