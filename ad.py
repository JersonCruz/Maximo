'Jerson Isaac cruz Albarrán'
'escribir un programa que calcule el maximo común divisor (MCD) de dos enteros positivos.'
def mcd (M,N):
    if N==0:
        return M
    else:
        return mcd(N,M%N)

num1 = int(input("Primer numero: "))
num2 = int(input("Segundo numero: "))

print("El maximo común divisor es ", mcd(num1,num2))