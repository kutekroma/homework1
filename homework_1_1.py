# 1. Создайте две переменных и введите в них данные с клавиатуры.
# Напишите простейший калькулятор, который умножает, делит, складывает,
# вычитает эти два числа, выведите результаты на экран.

# Выполнил Лазо Александр

import numbers

#функция для вычисления результата операций
def calc (first_number, second_number, math_action) -> [int | float]:
       match math_action:
            case "+":
                return (print(f"Результат сложения: {first_number+second_number}"))
            case "-":
                return (print(f"Результат вычитания: {first_number-second_number}"))
            case "*":
                return (print(f"Результат умножения: {first_number*second_number}"))
            case "/":
                try:
                    return (print(f"Результат деления: {first_number/second_number}"))
                #обрабатываем деление на ноль
                except ZeroDivisionError:
                    print(f"Деление на ноль запрещено")

if __name__ == '__main__':
    try:
        first_number = float(input("Введите первое число (целое или вещественное): "))
        if (isinstance(first_number, numbers.Number)):
            second_number = float(input("Введите второе число (целое или вещественное): "))
            if (isinstance(second_number, numbers.Number)):
                math_action = str(input("Введите математическое действие с числом: "))
                calc(first_number, second_number, math_action)
    #обрабатываем ввод не числа, а другого символа
    except ValueError:
        print(f"Вы ввели не числовое значение. Введите число, пожалуйста")



