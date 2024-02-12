from collections import Counter

def wordCount(t):
    # Read the contents of the file into a string
    with open(t, 'r') as file:
        text = file.read()

    # Split the text into individual words
    words = text.split()

    # Initialize an empty dictionary to store word counts
    word_count = {}

    # Count the occurrences of each word
    for word in words:
        word = word.lower()  # Convert to lowercase for case-insensitivity
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Print the individual word counts
    for word, count in word_count.items():
        print(f"'{word}' was found {count} times")

wordCount("file2.txt")