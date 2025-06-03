#Задача 3
#Сформувати матрицю 3х4 випадкових чисел в діапазоні (-6, 6). 
#Відсортувати кожний рядок за спаданням. 
#Знайти номер рядка з найбільшою медіаною.
#Роздрукувати підмасив 2х2 у верхньому лівому куту матриці. 
#Вилучити другий стовпчик масива.
#Оформити програму у вигляді головної програми і 3 підпрограм: 
# 1) введення (формування) вхідних даних; 2) розв’язання задачі; 3) виведення результату.

import numpy as np

def get_array():
    array = np.random.randint(-6, 7, size=(3,4))
    return array

def calc(array):
    sorted_array = np.flip(np.sort(array), axis=1)
    median_array = np.median(sorted_array, axis=1)
    row_with_max_median=np.argmax(median_array)
    array_part=sorted_array[:2,:2]
    array_part_del_col=np.delete(array_part, [1], axis=1)
    return [sorted_array, median_array, row_with_max_median, array_part, array_part_del_col]

def output_results(array, results):
    print("Оригінальна матриця:\n", array, sep="")
    print("\nМатриця після сортування рядків(за спаданням):\n", results[0], sep="")
    print("\nМедіани рядків:", results[1])
    print("Номер рядка з найбільшою медіаною:", results[2])
    print("\nПідмасив 2x2:\n", results[3], sep="")
    print("\nПідмасив без другого стовпця:\n", results[4], sep="")

array = get_array()
results = calc(array)
output_results(array, results)

