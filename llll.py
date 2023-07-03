# a = [1 , 2, 3, 4, 5]
# print('Сумма: ' + str(sum(a)))
# num1 = a[0]
# num2 = a[1]
# num3 = a[2]
# num4 = a[3]
# num5 = a[4]
# print('Сумма: ' + str(num1 + num2 + num3 + num4 + num5))

# list = ['молоко', 'хлеб', 'чай', 'вода', 'масло']
# list.pop(-1)
# list.pop(-2)
# list.append('яблоко')
# list.append('морковь')
# list.append('сыр')
# list.sort()
# list.pop(-1)
# print('Длина списка: ' + str(len(list)))
# print(list)



# def strcount(s):
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(f'{sym} - {counter}' )


# strcount('zxccc')


def strcount(s):
    sym_counter = {}
    for sym in s:
        sym_counter[sym] = sym_counter.get(sym, 0) + 1

    for sym, count in sym_counter.items():
        print(f'{sym} - {count}')

strcount('zxcuw9kjdhcc')





















