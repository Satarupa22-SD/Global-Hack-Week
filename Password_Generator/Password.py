import string
import random

if __name__ == "__main__":
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    password_len = int(input("Enter the length of the Password:- \n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    print("Your Password is:  ")
    print("".join(random.sample(s,  password_len)))

    