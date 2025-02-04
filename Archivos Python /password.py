import random

# Function that generates a random 15-character password
def generate_password():
    # Lists of possible characters for the password
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    symbols = ['!', '#', '$', '&', '/', '(', ')']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    # Combine all character lists into one
    characters = uppercase + lowercase + symbols + numbers

    # List to store the password characters
    password = []

    # Generate 15 random characters
    for i in range(15):
        random_character = random.choice(characters)  # Chooses a random character
        password.append(random_character)  # Adds the character to the list

    # Join the characters into a string and return it
    password = "".join(password)
    return password


def run():
    password = generate_password()  # Calls the function that generates the password
    print('Your new password is: ' + password)  # Displays the generated password

# Executes the 'run' function only if this file is run directly
if __name__ == '__main__':
    run()
