from sum_module import calc_sum_row

def calc_print_average(text, categories, years, data):
    print(f"\n--- Середня кількість злочинів за {text} ---")    
       
    for j in range(len(categories)):
        average = calc_sum_row(data)[j]/len(years)
        print(f"  {categories[j]:<10} :{average}")