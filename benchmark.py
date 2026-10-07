import time
import random

arr1=[]
import random

def generate_random_array(size):
    return random.choices(range(1_000_000), k=size)

x=generate_random_array(100)
print(x)
        