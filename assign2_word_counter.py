# Word Counter from Text File

# Open and read the text file
with open("sample.txt", "r") as file:
    text = file.read()

# Count words
words = text.split()
word_count = len(words)

# Count lines
lines = text.splitlines()
line_count = len(lines)

# Count characters
character_count = len(text)

# Display results
print("----- Word Counter -----")
print("Number of Words      :", word_count)
print("Number of Lines      :", line_count)
print("Number of Characters :", character_count)