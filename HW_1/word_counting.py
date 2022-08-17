import string

file = open("words.txt").read().lower()
for punctuation in string.punctuation:
    file = file.replace(punctuation, "")

file = file.split()

repeated_words = sorted(file)
unrepeated_words = sorted(set(repeated_words))

counts = []
for unrepeated in unrepeated_words:
    counter = 0
    for repeated in repeated_words:
        if repeated == unrepeated:
            counter += 1
    counts.append((counter, unrepeated))

counts.sort()
counts.reverse()
print(counts[0])
