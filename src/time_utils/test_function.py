from time_utils import measure_time

@measure_time.measure_time
def test_function(iter, divisor):
    for _ in range(0, iter):
        if _ % divisor == 0:
            print(_)

test_function(200000000, 2543)
