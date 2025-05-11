from categories_module import get_categories
from year_module import get_year_array
from input_module import input_data
from sum_module import calc_sum_column, calc_sum_row

#Введення категорій, років і статистичних даних до відповідних списків 
age_categories = get_categories("Вибір вікових категорій:", ["14-17 років", "18-29 років", "30+"])
sex_categories = get_categories("Вибір категорій статі:", ["Чоловіки", "Жінки"])

years = get_year_array()

age_data = input_data("за віковими категоріями", age_categories, years)
sex_data = input_data("за статевими категоріями", sex_categories, years)

#Oпрацювання даних та їх виведення
calc_print_percent("віковими категоріями", years, age_categories, age_data)
calc_print_percent("статевими категоріями", years, sex_categories, sex_data)

calc_print_average("за віковими категоріями",age_categories, years, age_data)
calc_print_average("за статевими категоріями", sex_categories,years, sex_data)
