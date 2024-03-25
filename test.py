def gen_fun(x):
    for i in range(x):
        yield i


result = gen_fun(10)
for items in result:
    print(items)

