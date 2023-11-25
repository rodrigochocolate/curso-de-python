a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print('Com os segmentos acima é possível formar um triângulo EQUILÁTERO')
    elif a != b and b != c and a != c:
        print('Com os segmentos acima é possível formar um triângulo ESCALENO')
    else:
        print('Com os segmentos acima é possível formar um triãngulo ISÓSCELES')
else:
    print('Não é possível formar um TRIÂNGULO!')