import random
from typing import List

Pack: List[str] = ["circle", "waves", "cross", "square", "triangle"] * 5


def random_pack(Pack: List[str]):
    return random.shuffle(Pack)
