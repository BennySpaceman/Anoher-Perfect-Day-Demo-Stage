import time
# starttime = time.time()
# print(simple_gcd(4,8))
# endtime = time.time()
# print(f'simple completed in {(endtime-starttime):.5} seconds')


def simple_gcd(a, b):
    starttime = time.time()
    candidates = []
    for i in range(1, min(a, b)):
        if (a % i ==0) and (b % i == 0):
            candidates.append(i)
    endtime = time.time()
    print(f'Simple completed in {endtime - starttime} seconds with a result of {candidates[-1]}')


def euclide_gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


simple_gcd(44444444, 33333333)

starttime = time.time()
print(f'Euclide result: {euclide_gcd(33333333, 44444444)}.', end=' ')
endtime = time.time()
print(f'Time: {(endtime-starttime):.5} seconds')
