#generator
def gen():
    for i in range(0,18):
        yield i
g=gen()
#methods to use generator

print(next(g))
print(next(g))

for j in g:
    print(j)
    
#function caching
import time
from functools import lru_cache
def fx(n):
    time.sleep(3)
    return n*5
print(fx(2))
print(fx(4))
print(fx(6))
print(fx(2))
print(fx(4))
print(fx(6))
