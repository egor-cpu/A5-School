import math
a = input()
isbn = a[:-1]
if len(isbn) == 9:
    sum_isbn = 0
    count = 10
    for i in isbn:
        if i == "X":
            i = 10
        sum_isbn += int(i) * count
        count -= 1
    if (11 - (sum_isbn % 11) == 10 and a[-1] == "X") or (str(11 - (sum_isbn % 11)) == a[-1]):
        print("valid")
    else:
        print("invalid")
elif len(isbn) == 12:
    f_sum = 0
    for i in isbn[::2]:
        if i == "X":
            i = 10
        f_sum += int(i)
    s_sum = 0
    for i in isbn[1::2]:
        if i == "X":
            i = 10
        s_sum += int(i)
    b = f_sum + s_sum * 3

    if (math.ceil(b / 10) * 10 - b) == int(a[-1]):
        print("valid")
    else:
        print("invalid")

