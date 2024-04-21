from time import time


def mierz_czas(function):
    def timing(*args, **kwargs):
        start_time = time()
        function(*args, **kwargs)
        end_time = time()

        print(f"Function {function.__name__} took {round(end_time - start_time, 2)}s to execute.")

    return timing
