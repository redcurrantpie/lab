from categories_module import get_categories
from year_module import get_year_array
from input_module import input_data
from sum_module import calc_sum_column, calc_sum_row

age_categories = get_categories("Вибір вікових категорій:", ["14-17 років", "18-29 років", "30+"])
sex_categories = get_categories("Вибір категорій статі:", ["Чоловіки", "Жінки"])

years = get_year_array()

age_data = input_data("за віковими категоріями", age_categories, years)
sex_data = input_data("за статевими категоріями", sex_categories, years)

#Oпрацювання даних




def calc_print_percent(text, years, categories, data):
    print(f"\n--- Відсотковий розподіл за {text} ---")

    for i, year in enumerate(years):
        print(f"\n{year} рік:")
        for j, categorie in enumerate(categories):
            percent = data[j][i]*100/calc_sum_column(data)[i]
            print(f"  {categorie}: {round(percent,2)}%")

calc_print_percent("віковими категоріями", years, age_categories, age_data)
calc_print_percent("статевими категоріями", years, sex_categories, sex_data)


def calc_print_average(text, categories, years, data):
    print(f"\n--- Середня кількість злочинів за {text} ---")    
       
    for j in range(len(categories)):
        average = calc_sum_row(data)[j]/len(years)
        print(f"  {age_categories[j]} :{average}")

calc_print_average("за віковими категоріями",age_categories, years, age_data)
calc_print_average("за статевими категоріями", sex_categories,years, sex_data)
