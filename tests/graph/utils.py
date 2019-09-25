import os
from pathlib import Path


def generate_path(_input):
    root_dir = Path(__file__).resolve().parents[0]
    file_path = os.path.join(root_dir, _input)
    return file_path
