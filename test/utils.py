import string
from random import shuffle


def file_reader(file_name='./test/test.txt'):
    words = []
    with open(file_name, 'r') as file:
        for line in file:
            for word in line.split():
                word = word.strip(string.punctuation).lower()
                words.append(word)
    return word


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


def initiate(st_class):
    words = ascii_generator()
    st = st_class()
    frequency_counter(st, words)
    return st
