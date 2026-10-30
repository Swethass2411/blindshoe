import glob

for folder in ["train/labels", "valid/labels", "test/labels"]:
    for file in glob.glob(folder + "/*.txt"):

        lines = []

        with open(file, "r") as f:
            data = f.readlines()

        for line in data:
            parts = line.strip().split()

            if parts:
                if parts[0] == "20":
                    parts[0] = "19"

                lines.append(" ".join(parts) + "\n")

        with open(file, "w") as f:
            f.writelines(lines)

print("Dustbin class merged: ID 20 → ID 19")