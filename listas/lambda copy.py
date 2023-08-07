def somar(x):
    def func2(x): return x+10
    return func2(x)*4


print(somar(2))
