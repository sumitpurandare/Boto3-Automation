from random import choice

len_of_pass = 16

chars = "abcdefghijklmnopqrstvuwxyz1234567890!@#$%^&*()_+><>~ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# password = []
# for each_char in range(len_of_pass):
#     password.append(choice(chars))

# print("Your random password is :" ,"".join(password))

random_pass = "".join(choice(chars) for each in range(len_of_pass))
print("Your random password is : "+random_pass)