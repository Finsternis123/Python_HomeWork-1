# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
n = int(input('Specify size n:'))
m = int(input('Specify size m:'))
k = int(input('Specify the number of slices k:'))

if k <= m * n and (k % m == 0 or k % n == 0):
    print('True')
else:
    print('False')