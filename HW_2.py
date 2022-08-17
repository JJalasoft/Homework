import argparse
import string


#terminal flags
parser = argparse.ArgumentParser(description = "Count words in text")
parser.add_argument('-w', '--word', type=str, help='Receive a word to count it in the text file')
args = parser.parse_args()

words_to_count = args.word
#---------------------
filename = "romeo.txt"

def remove_puncts_from_file(filename):
    file = open(filename, "r").read().lower()

    for punctuation in string.punctuation:
        file = file.replace(punctuation, "")
    return file

def words_counting(text):
    repeated_words = text.split()
    unique_words = sorted(set(repeated_words))

    words_count = {}
    for unrepeated in unique_words:
        counter = 0
        for repeated in repeated_words:
            if repeated == unrepeated:
                counter += 1
        words_count[unrepeated] = counter
    return words_count

text = remove_puncts_from_file(filename)
word_count = words_counting(text)
print(word_count[str(words_to_count)])
