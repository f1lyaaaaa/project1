
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

def main():
    print("Калькулятор")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    choice = input("Выберите операцию (1-4): ")

    if choice not in ('1', '2', '3', '4'):
        print("Неверный выбор")
        return

    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: введите число")
        return

    if choice == '1':
        print(f"Результат: {add(a, b)}")
    elif choice == '2':
        print(f"Результат: {subtract(a, b)}")
    elif choice == '3':
        print(f"Результат: {multiply(a, b)}")
    elif choice == '4':
        print(f"Результат: {divide(a, b)}")

if __name__ == "__main__":
    main()
