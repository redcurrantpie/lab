import numpy as np

def input_data():
    arr = np.random.randint(2, 8, size=15)
    return arr
                
def calc(array):
    mean = np.mean(array)
    median = np.median(array)
    def modes(array):
        dic_quantites={}
        for num in array:
            dic_quantites[num] = dic_quantites.get(num, 0)+1
        max_quantity = max(dic_quantites.values())
        modes = [int(k) for k, v in dic_quantites.items() if v == max_quantity]
        return modes
    return mean, median, modes(array)

def output_result(array, mean, median, mode):
    print(f"Cформований масив:\n  {array}")
    print("\nРезультати обчислень:")
    print(f"  Середнє арифметичне: {mean:.2f}")
    print(f"  Мода: {mode}")
    print(f"  Медіана: {median}")
        
arr=input_data()
mean, median, mode = calc(arr)
output_result(arr, mean, median, mode)
   
 
 

