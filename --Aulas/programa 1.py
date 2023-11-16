import numpy as np

a = float(input("Digite a: "))
b = float(input("digite b: "))
c = float(input("digite c: "))

limi = float(input("Digite o limite inferior: "))
lims = float(input("Digite o limite superior: "))


def procuraIntervalo(a,b,c):

    def f(a,b,c,x):
        return a*x**2+b*x+c, x

    x = -10
    funcao1, xis1 = f(a, b, c, x)

    x += 2
    funcao2, xis2 = f(a,b,c,x)

    if funcao1*funcao2 < 0:
        return xis1, xis2
    else:
        return ""