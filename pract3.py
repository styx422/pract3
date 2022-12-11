n=int(input(('Введите количество элементов:  ')))
posl = []
for i in range (n):
    while len(posl) <= n-1:
        posl.append((int(input('Введите элементы последовательности, по одному:  '))))
print('Задан массив: ')
print(posl)
sposl = sorted(posl)
print('Отсортированный массив:')
print(sposl)
a = int(input(('Введите число, для проверки:  ')))
start = 0
end = len(sposl) - 1
mid = len(sposl) // 2
k = 3

while sposl[mid] != a and start <= end:
    if a > sposl[mid]:
        start = mid + 1
    else:
        end = mid - 1
    mid = (start + end) // 2
    k += 1
if a not in sposl:
    print('Числа', a, 'нет в массиве')
    print('Количество шагов для нахождения числа', a,':', k)
else:
    print('Число', a ,'есть в массиве')
    print('Количество шагов для нахождния числа', a, ':', k)
