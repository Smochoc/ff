

# def strcount(s):
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(f'{sym} - {counter}' )


# strcount('zxccc')


# def strcount(s):
#     sym_counter = {}
#     for sym in s:
#         sym_counter[sym] = sym_counter.get(sym, 0) + 1

#     for sym, count in sym_counter.items():
#         print(f'{sym} - {count}')

# strcount('zxcuw9kjdhcc')




word = input("Введите  слово: ")
lenn = len(word) - 1
a = 0
stop = 0

# reverse = reversed(word)
# if len(word) % 2 != 0:
# word_lst = list(word)

while lenn - a >= a:
    if word[lenn - a] == word[a]:
        a += 1

    else:
        stop = 1
        print("False")
        break


if stop == 0:
    print("True")



