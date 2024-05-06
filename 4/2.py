from typing import Generator


def fib_generator(n: int) -> Generator[int, None, None]:
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1