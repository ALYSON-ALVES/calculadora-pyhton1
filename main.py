n1 = int(input('digite um número: ' ))
n2=int(input('digite o segundo número: '))
soma =n1+n2
subtraçao=n1-n2
multiplicação=n1*n2

print(f'a soma é igual a: {soma}')

print(f'a subtração é igual a: {subtraçao}')

print(f'a multiplicação é igual a: {multiplicação}')
if n2 !=0:
    divisão= n1/n2
    print(f'a divisão é : {divisão}')
else:
    print('não é possível dividir por zero')
    