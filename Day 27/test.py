def add(*args):
    print(args, type(args))
    sum = 0
    for num in args:
        sum += num

    return sum

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))

def calculate(**kwargs):
    print(kwargs,type(kwargs))

calculate()