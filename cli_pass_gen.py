import random
import string
random_number = random.randint(0, 5)
given_length = 15
input_text = input('some text here :')
length_now = len(input_text)
print('length_now: ', length_now)
if length_now < given_length:
    valency = given_length - length_now
    print('valency: ', valency)
else:
    valency = 0
    print('valency: ', valency)
random_prefixes = random.choices(string.ascii_letters, k=valency)
input_text = ''.join(random_prefixes)+"_" + input_text
print('input_text: ', input_text)

input_text = '3'.join(input_text.rsplit('e', 1))
input_text = '!'.join(input_text.rsplit('i'))
my_str = input_text.replace('a', '@', 1).replace('l', '1', 1).replace('o', '0', 1).replace('s', '&', 1).replace(
    't', '7', 1).replace('g', '9', 1).replace('S', '$', 1).replace('h', '#', 1).replace(" ", "-", random_number).replace(" ", "_")
print('my_str: ', my_str)
