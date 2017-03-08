
"""
Your task is to write a higher order function for chaining together a list of unary functions. In other words, it should return a function that does a left fold on the given functions.

chained([a,b,c,d])(input)
Should yield the same result as

d(c(b(a(input))))

"""


def chained(functions):
    for func in functions:
        func(functions[functions.index(func):])
    return None


def f1(x): return x*2
def f2(x): return x+2
def f3(x): return x**2

def f4(x): return x.split()
def f5(xs): return [x[::-1].title() for x in xs]
def f6(xs): return "_".join(xs)

if __name__ == "__main__":
    print(chained([f1, f2, f3])(0))