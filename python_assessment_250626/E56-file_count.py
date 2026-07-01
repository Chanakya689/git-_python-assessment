#Given Input (sample.txt):
#Hello World
#Python is fun.
#Expected Output: Lines: 2 | Words: 5 | Characters: 27

with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    line_count = len(lines)
    print(line_count)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)

print(f"Lines: {line_count} | Words: {word_count} | Characters: {char_count}")