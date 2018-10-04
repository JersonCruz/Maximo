'Jerson Isaac cruz Albarrán'
def mcd (a,b):
    if b==0:
        return a
    else:
        return mcd(b,a%b)

num1 = int(input("Primer numero: "))
num2 = int(input("Segundo numero: "))

print("El maximo común divisor es ", mcd(num1,num2))