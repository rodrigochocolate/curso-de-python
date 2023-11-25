import math
an = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(an))
print(f'O ângulo de {an} tem o SENO de {sen:.2f}')
cos = math.cos(math.radians(an))
print(f'O ângulo de {an} tem o COSSENO de {cos:.2f}')
tan = math.tan(math.radians(an))
print(f'O ângulo de {an} tem o TANGENTE de {tan:.2f}')