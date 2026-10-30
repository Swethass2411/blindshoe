import glob

# Old class ID -> New class ID
mapping = {
    0:0,
    1:1,
    2:2,
    3:3,
    5:4,
    6:5,
    7:6,
    9:7,
    10:8,
    11:9,
    12:10,
    13:11,
    14:12,
    15:13,
    16:14,
    17:15,
    18:16,
    19:17,
    21:18,
    22:19,
    26:20,
    27:21,
    28:22,
    29:23,
    30:24,
    31:25,
    32:26,
    33:27,
    34:28
}

for folder in ["train/labels", "valid/labels", "test/labels"]:

    for file in glob.glob(folder + "/*.txt"):

        new_lines = []

        with open(file, "r") as f:
            lines = f.readlines()

        for line in lines:
            parts = line.strip().split()

            if parts:
                old_id = int(parts[0])

                if old_id in mapping:
                    parts[0] = str(mapping[old_id])
                    new_lines.append(" ".join(parts) + "\n")

        with open(file, "w") as f:
            f.writelines(new_lines)

print("All class IDs remapped successfully")