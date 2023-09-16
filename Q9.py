import string

def is_pangram(string):
    return set(string.lower()) >= set(string.ascii_lowercase)

# Example usage:
text = "The quick brown fox jumps over the lazy dog"
if is_pangram(text):
    print("The text is a pangram.")
else:
    print("The text is not a pangram.")
