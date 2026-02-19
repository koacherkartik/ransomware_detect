import math
from collections import Counter

def calculate_entropy(file_path):
    """
    Calculates Shannon entropy of a file.
    High entropy indicates encrypted or compressed data.
    """
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        if not data:
            return 0.0

        counts = Counter(data)
        entropy = 0.0
        for count in counts.values():
            p = count / len(data)
            entropy -= p * math.log2(p)

        return round(entropy, 3)

    except Exception as e:
        return -1
