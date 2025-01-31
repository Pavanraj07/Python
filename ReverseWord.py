# Reverse the words in a sentence
sentence = input("Enter a sentence: ")
reversed_sentence = ' '.join(sentence.split()[::-1])
print(f"Reversed sentence: {reversed_sentence}")
