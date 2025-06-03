#3. Створити датафрейм з даними про продажі товарів в онлайн-магазині: 
#CustomerID, ProductName, Quantity, Price, Country, OrderDate 
#Додати новий стовпчик TotalSum – загальна сума придбаних товарів (=Quantity* Price). 
#Визначити товар, за який сплачено найбільшу суму. 
#Визначити суму грошей, які витрачені заданою країною за певний проміжок часу.
#Оформити програму у вигляді головної програми і 3 підпрограм: 1) введення (формування) вхідних даних; 2) розв’язання задачі; 3) виведення результату.

import pandas as pd
import numpy as np

def input_data():
    orders=pd.DataFrame({"OrderID":np.arange(34121, 34127),
                        "CustomerID":np.arange(12121, 12127),
                        "Country":["Україна", "Польща", "Німеччина", "Казахстан", "Болівія", "Україна"],
                        "OrderDate":["24-08-13","24-11-13","25-01-30","25-01-31","25-03-13","25-03-13"]})

    order_items=pd.DataFrame({"OrderID":[34121, 34122, 34123, 34123, 34124, 34124, 34124, 34125, 34126],
                        "ProductName":["Гармошка","Калейдоскоп", "Картон", "Глина", "Відерця", "Гірка","Екскаватор", "Лялька-неваляйка", "Пелюшки"],
                        "Quantity":[1, 1, 6, 3, 2, 1, 1, 4, 10],
                        "Price":[350, 217, 15, 50, 70, 689, 150, 270, 130]})
    return orders, order_items

def process_data(order_items, orders, country, start_date, end_date):
    df=order_items.merge(orders, on="OrderID")
    df['OrderDate'] = pd.to_datetime(df['OrderDate'], format="%y-%m-%d")
    df["TotalSum"]=df["Quantity"]*df["Price"]

    #Найдорожчий товар
    max_paid_product = df.loc[df["TotalSum"] == df["TotalSum"].max(), "ProductName"]

    #Фільтрація 
    try:
        start = pd.to_datetime(start_date, format="%y-%m-%d")
        end = pd.to_datetime(end_date, format="%y-%m-%d")
    except ValueError:
        print("Невірний формат дати. Має бути yy-mm-dd.")
        return df, max_paid_product, 0

    filtered = df[(df["Country"] == country) &
                     (df["OrderDate"] >= start) &
                     (df["OrderDate"] <= end)]
    
    total_by_country = filtered["TotalSum"].sum()
    return df, max_paid_product, total_by_country

def output_results(df, max_product, total_by_country):
    print(df)
    print(f"\nНайдорожчий товар за TotalSum: {','.join(max_product)}")
    print("\nЗагальна сума покупок у вибраній країні за вказаний період:", total_by_country)

order_items, orders = input_data()

print("\nВведіть дані для фільтрації (Enter для значень за замовченням):")
country = input("Країна [Україна]: ") or "Україна"
start_date = input("Початкова дата (yy-mm-dd) [25-01-31]: ") or "25-01-31"
end_date = input("Кінцева дата (yy-mm-dd) [25-03-13]: ") or "25-03-13"

df, max_product, total_by_country = process_data(order_items, orders, country, start_date, end_date)
output_results(df, max_product, total_by_country)

