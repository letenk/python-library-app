import random
import string

def random_string(panjang:int) -> str:
    return ''.join(random.choice(string.ascii_letters) for i in range(panjang))