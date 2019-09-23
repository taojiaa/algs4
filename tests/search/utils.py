import string
from random import shuffle


def read_string_array(file_path):
    words = []
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                word = word.strip(string.punctuation).lower()
                words.append(word)
    return words


def frequency_counter(st, words, min_len=0):
    for word in words:
        if len(word) < min_len:
            continue
        if st.contains(word):
            st.put(word, st.get(word) + 1)
        else:
            st.put(word, 1)


def ascii_generator():
    ascii_str = string.ascii_lowercase
    words = []
    for i, char in enumerate(ascii_str):
        words = words + [char] * (i + 1)
    shuffle(words)
    return words
