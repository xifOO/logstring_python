def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} была вызвана с позиционными аргументами {args} и именованными аргументами {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def fib_generator(n: int) -> list[int]:
    a, b = 1, 1
    count = 0
    fib_sequence = []
    while count < n:
        fib_sequence.append(a)
        a, b = b, a + b
        count += 1
    return fib_sequence


fibonacci = fib_generator(10)
print(fibonacci)
