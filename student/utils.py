import random
import string

def key_generator(model):
    key = ''.join(random.choice(string.digits) for x in range(6))
    if model.objects.filter(randomly_generate_id=key).exists():
        key = key_generator()
    return key
