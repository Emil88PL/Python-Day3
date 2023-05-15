def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

with open("words.txt") as f:
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
    per = 100 * count_char(text, char) /len(text)
    print("{0} - {1}".format(char, round(per, 2)))

