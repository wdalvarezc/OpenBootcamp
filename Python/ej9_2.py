from functools import reduce
def sumaImpares(a):
    impares = filter(lambda x: (x%2 == 1),a)
    impares = list(impares)
    suma = reduce(lambda a,b: a+b,impares)
    print(f'el resultado es: {suma}')

sumaImpares([1,2,3,7,9,4,6]) ### output => el resultado es :20