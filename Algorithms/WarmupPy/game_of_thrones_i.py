def check_is_palindrome(token):
    count = 0
    palindrome_memory = {}

    for letter in list(token):
        if letter in palindrome_memory:
            count += 1
            del palindrome_memory[letter]
        else:
            palindrome_memory[letter] = 1

    return 'YES' if count == len(token)/2 else 'NO'

print check_is_palindrome(raw_input())
