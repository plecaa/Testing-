# 5-digit PIN we want to "crack"
password = "25083"  # you can change this

# Open a file to store all possible 5-digit combinations
with open("pin_combinations.txt", "w") as file:
    # Generate all 5-digit PINs from 00000 to 99999
    for pin in range(100000):
        guess = str(pin).zfill(5)  # make sure it's 5 digits, e.g., '00001'
        file.write(guess + "\n")   # save to file

# Now, check the file against the password
with open("pin_combinations.txt", "r") as file:
    for line in file:
        attempt = line.strip()  # remove newline character
        if attempt == password:
            print("Password found! ->", attempt)
            break