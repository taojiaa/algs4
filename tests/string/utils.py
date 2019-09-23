import os
import string
from pathlib import Path


def generate_path(_input):
    root_dir = Path(__file__).resolve().parents[0]
    file_path = os.path.join(root_dir, _input)
    return file_path


def stripped_lines(f):
    return (l.rstrip("\n") for l in f)


def read_string_array(file_path):
    file_path = generate_path(file_path)
    words = []
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                word = word.strip(string.punctuation).lower()
                words.append(word)
    return words
