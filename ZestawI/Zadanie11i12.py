p = 1
for i in range(10):
    print(p)
    p += 1


# Zadanie12

def frange(start, stop, step):
    i = start
    while i > stop:
        yield i
        i -= step


for i in frange(100, 20, 5):
    print(i)
