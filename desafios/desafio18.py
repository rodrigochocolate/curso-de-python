from math import sin, cos, tan, radians
n1 = float(input('Digite um ângulo qualquer: '))
seno = sin(radians(n1))
coss = cos(radians(n1))
tang = tan(radians(n1))
print(f'O seno desse ângulo é {seno:.2f}')
print(f'O cosseno desse ângulo é {coss:.2f}')
print(f'O tangente desse ângulo é {tang:.2f}')
