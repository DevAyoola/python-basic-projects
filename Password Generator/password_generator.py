# Password Generator

import random

pass_len = int(input("Enter the length of the password: "))

pass_char = "qwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+-=[];',./\:<>?"

password = "".join(random.sample(pass_char, pass_len))

print(password)