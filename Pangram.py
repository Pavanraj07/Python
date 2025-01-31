# Check if a string is a pangram (contains all letters of the alphabet)
import string

def is_pangram(sentence):
    return set(string.ascii_lowercase).issubset(set(sentence.lower()))

text = input("Enter a sentence: ")
if is_pangram(text):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
