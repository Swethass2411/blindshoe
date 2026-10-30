from collections import Counter
import glob
import os

found = 0

for f in glob.glob("valid/labels/*.txt"):
    with open(f, errors="ignore") as file:
        lines = [x.strip() for x in file if x.strip()]

    counts = Counter(lines)

    duplicates = [x for x, n in counts.items() if n > 1]

    if duplicates:
        print(os.path.basename(f))
        print("Duplicates:", duplicates)
        found += 1

print("Total files with duplicate labels:", found)