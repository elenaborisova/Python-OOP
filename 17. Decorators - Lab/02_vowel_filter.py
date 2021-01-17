from functools import wraps


def vowel_filter(func):
    @wraps(func)
    def wrapper():
        vowels = {"a", "e", "o", "u", "y", "i"}
        func_letters = func()
        filtered_vowels = [letter for letter in func_letters if letter.lower() in vowels]
        return filtered_vowels

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


@vowel_filter
def get_name():
    return "Elena"


print(get_letters)
print(get_letters())
print(get_name())
