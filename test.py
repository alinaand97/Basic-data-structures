#Задача 1: Арифметика
result = 9 ** 0.5 * 5
print(result)

#Задача 2: Логика
result = (9.99 > 9.98) and (1000 != 1000.1)
print(result)

#Задача 3: Школьная загадка
expression1 = 2 * 2 + 2  # без приоритета
expression2 = 2 * (2 + 2)  # с приоритетом
print(expression1)
print(expression2)
comparison_result = (expression1 == expression2)
print(comparison_result)

#Задача 4: Первый после точки
number_str = '123.456'
number_float = float(number_str)  # Преобразуем строку в дробное число
shifted_number = number_float * 10  # Умножаем на 10
int_part = int(shifted_number)  # Берем целую часть
first_digit_after_decimal = int_part % 10  # Остаток от деления на 10
print(first_digit_after_decimal)  # Выводим первую цифру после точки

