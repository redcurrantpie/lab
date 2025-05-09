def input_radiation_every_hour():
    radiation_levels = []  
    for hour in range(24):
        while True:
            try:
                value=float(input(f"Введіть рівень радіації o {hour}.00 годині: " ))
                if value >= 0:
                    radiation_levels.append(value)
                    break
                else:
                    print("Число має бути ≥ 0")
            except ValueError:
                value =float(input(f"Некоректне значення. Спробуйте ще раз. " ))
    return radiation_levels
