s = 0
v = 0
for c in range(0, 501, 3):
    if c % 2 != 0:
        s += c
        v += 1
print(f'Entre 0 e 500 foram somados {v} valores e a soma entre eles é {s}')
