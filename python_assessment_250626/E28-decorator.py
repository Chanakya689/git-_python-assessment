import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"Function '{func.__name__}' took {end - start:.4f} seconds to run.")
        return result

    return wrapper

@timer
def waste_time():
    time.sleep(1.5)

waste_time()