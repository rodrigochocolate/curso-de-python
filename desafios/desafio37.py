n = int(input('Digite um número: '))
print('''------------------
[ 1 ] binário
[ 2 ] octal
[ 3 ] hexadecimal
------------------''')
escolha = int(input('Escolha a base da conversão: '))
if escolha == 1:
    print(f'{n} convertido para BINÁRIO é {bin(n)[2:]}')
elif escolha == 2:
    print(f'{n} convertido para OCTAL é {oct(n)[2:]}')
else:
    print(f'{n} convertido para HEXADECIMAL é {hex(n)[2:]}')
