import random
import string

#create a random string with digits and letters
def random_string(letter_count, digit_count):
    string_one = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))
    string_one += ''.join((random.choice(string.digits) for x in range(digit_count)))

    sam_list = list(string_one)
    random.shuffle(sam_list)
    final_string = ''.join(sam_list)
    return final_string

#create a random numbers with digits only
def random_number(digits_count):
    string_one = ''.join((random.choice(string.digits) for x in range(digits_count)))

    sam_list = list(string_one)
    random.shuffle(sam_list)
    final_string = ''.join(sam_list)
    return final_string

#print(random_number(3))