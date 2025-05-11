from sum_module import calc_sum_column

def calc_print_percent(text, years, categories, data):
    print(f"\n--- Відсотковий розподіл за {text} ---")

    for i, year in enumerate(years):
        print(f"\n{year} рік:")
        for j, categorie in enumerate(categories):
            percent = data[j][i]*100/calc_sum_column(data)[i]
            print(f"  {categorie:<10}: {round(percent,2)}%")