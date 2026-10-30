import time
import sys

from task2 import run as run2
from task3 import run as run3

FILE_NAME = sys.argv[1] if len(sys.argv) > 1 else "schedule"
ITERATIONS = int(sys.argv[2]) if len(sys.argv) > 1 else 100

def time_custom():
    start = time.time()
    for _ in range(ITERATIONS):
        run2(FILE_NAME)

    return time.time() - start

def time_libs():
    start = time.time()
    for _ in range(ITERATIONS):
        run3(FILE_NAME)
    return time.time() - start

run2(FILE_NAME)
run3(FILE_NAME)

time_custom = time_custom()
time_libs = time_libs()

print(f"Собственный код:\t{time_custom:.4f} сек.")
print(f"Готовые библиотеки:\t{time_libs:.4f} сек.")
print(f"Разница:\t\t{time_custom / time_libs:.2f}x")
