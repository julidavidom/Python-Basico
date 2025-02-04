# Function that checks if a word or phrase is a palindrome
def palindrome(word):
    word = word.replace(' ', '')  # Removes spaces
    word = word.lower()  # Converts everything to lowercase
    reversed_word = word[::-1]  # Reverses the string

    return word == reversed_word  # Returns True if it is a palindrome, False if not

# Main function that asks for a word and checks if it is a palindrome
def run():
    word = input('Enter a word: ')
    if palindrome(word):
        print('It is a palindrome')
    else:
        print('It is not a palindrome')


if __name__ == '__main__':
    run()

