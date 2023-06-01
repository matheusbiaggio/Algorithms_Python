def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if len(word) == 1:
        return True
    elif len(word) == 2:
        return word[0] == word[1]
    elif word[0] != word[-1]:
        return False
    else:
        return is_palindrome_recursive(word[1:-1], low_index, high_index)
