def input_data(text, categories, years):
    print(f"\n--- Введення даних за {text} ---")
    data=[]
    for categorie in categories:
        row=[]
        for year in years:
            number=int(input(f"{categorie}, {year} рік: "))
            row.append(number)
        data.append(row)
    return data       