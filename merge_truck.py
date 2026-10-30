import glob

for folder in ["train/labels", "valid/labels", "test/labels"]:
    for file in glob.glob(folder + "/*.txt"):

        lines = []

        with open(file, "r") as f:
            data = f.readlines()

        for line in data:
            parts = line.strip().split()

            if parts:
                if parts[0] == "25":
                    parts[0] = "14"

                lines.append(" ".join(parts) + "\n")

        with open(file, "w") as f:
            f.writelines(lines)

print("Truck class merged: ID 25 → ID 14")