from input_module import input_radiation_every_hour
from avr_module import calc_average_radiation
from speed_module import calc_average_speed

#Введення даних
radiation_data = input_radiation_every_hour()

#Обчислення
avr = calc_average_radiation(radiation_data)
speed = calc_average_speed(radiation_data) 

#Виведення 
print("Cередньодобовий рівень радіації: ", round(avr, 2))
if speed >= 0:
    print("Cередня швидкість підвищення рівня радіації: ", round(speed, 3))
else:
    print("Cередня швидкість зниження рівня радіації: ", round(speed, 3))
