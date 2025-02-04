# Check if a character is a vowel or consonant
char = input("Enter a character: ").lower()
if char in "aeiou":
    print("Vowel")
elif char.isalpha():
    print("Consonant")
else:
    print("Not a letter")
