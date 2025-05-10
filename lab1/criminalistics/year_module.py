def get_year_array():
    year_fisrt = int(input("\nВведіть початковий рік: "))
    year_last = int(input("Введіть кінцевий рік:  "))

    if year_fisrt > year_last:
        year_fisrt, year_last = year_last, year_fisrt
        
    year_diapason = year_last - year_fisrt + 1
    return [year_fisrt + i for i in range(year_diapason)]
