#Задача 3.
#Сформувати матрицю 3х4 випадкових чисел в діапазоні (-6, 6). 
#Відсортувати кожний рядок за спаданням. 
#Знайти номер рядка з найбільшою медіаною.
#Роздрукувати підмасив 2х2 у верхньому лівому куту матриці. Вилучити другий стовпчик масива.

import torch

def get_tensor():
    tensor = torch.randint(-6, 7, (3, 4), dtype=torch.int)
    return tensor

def process_tensor(tensor):
    sorted_tensor, _ = torch.sort(tensor, dim=1, descending=True)
    medians = sorted_tensor.median(dim=1).values
    row_with_max_median = torch.argmax(medians).item()
    sub_tensor = sorted_tensor[:2, :2]
    tensor_without_second_col = sorted_tensor.index_select(1, torch.tensor([0, 2, 3]))
    return sorted_tensor, medians, row_with_max_median, sub_tensor, tensor_without_second_col

def print_results(original, sorted_tensor, medians, row_max, sub_tensor, no_second_col):
    print("Оригінальна матриця:\n", original)
    print("\nМатриця після сортування рядків (за спаданням):\n", sorted_tensor)
    print("\nМедіани рядків:", medians)
    print("Номер рядка з найбільшою медіаною:", row_max)
    print("\nПідмасив 2x2 (верхній лівий кут):\n", sub_tensor)
    print("\nМатриця без другого стовпця:\n", no_second_col)

tensor = get_tensor()
sorted_tensor, medians, row_max, sub_tensor, no_second_col = process_tensor(tensor)
print_results(tensor, sorted_tensor, medians, row_max, sub_tensor, no_second_col)
