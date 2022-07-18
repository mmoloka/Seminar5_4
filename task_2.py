# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#     1) с помощью математических формул нахождения корней квадратного уравнения
#     2) с помощью дополнительных библиотек Python

a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4*a*c
if D == 0:
    print(f'Один корень и он равен = {round(-b/2* a, 2)}')
elif D < 0:
    print('Корней нет')
else:
    print(f'Первый корень равен = {round((-b + D ** 0.5) / (2 * a), 2)}')
    print(f'Второй корень равен = {round((-b - D ** 0.5) / (2 * a), 2)}')

