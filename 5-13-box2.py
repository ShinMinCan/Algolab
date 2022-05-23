def box2(x):
    a = int((x - 2) / 2)
    b = int(x / 2) + 1
    for i in range(1, x + 1):
        if i == 1 or i == x:
            print("+" + "-" * a + "+" + "-" * a + "+")
        elif i == b:
            print("+" + "-" * a + "*" + "-" * a + "+")
        elif 1 < i < b:
            print("|" + "." * (i - 2) + "\\" + "." * (a + 1 - i), end="")
            print("|" + "." * (a + 1 - i) + "/" + "." * (i - 2) + "|")
        elif b < i < x:
            print("|" + "." * int(a + 1 - (i - a - 1)) + "/" + "." * int((i - a - 1) - 2), end="")
            print("|" + "." * int((i - a - 1) - 2) + "\\" + "." * int(a + 1 - (i - a - 1)) + "|")





n = int(input())
while n:
    t = int(input())
    box2(t)
    n -= 1