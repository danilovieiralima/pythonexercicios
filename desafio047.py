# from time import sleep
# for c in range(0, 51, 2):
#    print(c), sleep(0.5)
# print('Esses são todos os pares de 1 até 50')
from time import sleep

for n in range(0, 51):
    if n % 2 == 0:
        print(n, end=' '), sleep(0.5)
