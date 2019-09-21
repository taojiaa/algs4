import os
from pathlib import Path


def construct_graph(_input, g_class):
    if isinstance(_input, int):
        return g_class(_input)
    else:
        root_dir = Path(__file__).resolve().parents[0]
        file_path = os.path.join(root_dir, _input)
        return g_class(file_path)
