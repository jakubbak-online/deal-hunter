from mierz_czas import mierz_czas

@mierz_czas
def testowa_funkcja(iter, divisor):
    for _ in range(0, iter):
        if _ % divisor == 0:
            print(_)

testowa_funkcja(200000000, 2543)
