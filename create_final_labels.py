import os
import glob

BACKUP = r"..\Combined_Dataset _BACKUP"
FINAL = r"..\Final_Dataset"

mapping = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 1,
    5: 4,
    6: 5,
    7: 6,
    8: 2,
    9: 7,
    10: 8,
    11: 9,
    12: 10,
    13: 11,
    14: 12,
    15: 13,
    16: 14,
    17: 15,
    18: 16,
    19: 17,
    20: 18,
    21: 19,
    22: 20,
    23: 6,
    24: 9,
    25: 12,
    26: 21,
    27: 22,
    28: 23,
    29: 24,
    30: 25,
    31: 26,
    32: 27,
    33: 28,
    34: 29
}

for split in ["train", "valid", "test"]:
    source = os.path.join(BACKUP, split, "labels")
    destination = os.path.join(FINAL, split, "labels")

    os.makedirs(destination, exist_ok=True)

    for file in glob.glob(os.path.join(source, "*.txt")):
        output_file = os.path.join(
            destination,
            os.path.basename(file)
        )

        new_lines = []

        with open(file, "r") as f:
            for line in f:
                parts = line.strip().split()

                if not parts:
                    continue

                old_id = int(parts[0])

                if old_id not in mapping:
                    print("WARNING:", old_id, file)
                    continue

                parts[0] = str(mapping[old_id])
                new_lines.append(" ".join(parts) + "\n")

        with open(output_file, "w") as f:
            f.writelines(new_lines)

print("Final labels created successfully.")