import random
import string

def random_user_id():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=6))

# Example usage:
if __name__ == "__main__":
    print(random_user_id())
print(random.random())  # prints a random float between 0.0 and 1.0