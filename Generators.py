# def fun():
#     for i in range(5):
#          yield i


# gen=fun()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


def read_lines(filename):
    with open(filename) as file:
        for line in file:
            yield line.strip()


gen=read_lines("products_practice.csv")

for i in range(9):
    print(next(gen))
