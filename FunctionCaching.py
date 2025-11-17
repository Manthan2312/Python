from functools import lru_cache
from time import sleep

@lru_cache(maxsize=None)
def facto(number):
    facto_n=1
    sleep(5)
    for i in range(1,number+1):
        facto_n*=i
    return facto_n

print(facto(5))
print(facto(6))
print(facto(5))

