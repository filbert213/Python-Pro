import random
x = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("Enter the length of the password you want: "))
password = "".join(random.sample(x, int(length))) 

if int(length) > len(x):
    print("Error: Length exceeds the number of unique characters available.")
elif int(length) <= 0:
    print("Error: Length must be a positive integer.")
else:
    print("Your password is: ", password)

# This code generates a random password of a specified length using a mix of characters.
# It prompts the user to input the desired length and then creates a password accordingly.
# Note: Ensure that the input length does not exceed the number of unique characters in 'x' to avoid errors.



#other code options 
#for i in range(length):
#    password += random.choice(x)
