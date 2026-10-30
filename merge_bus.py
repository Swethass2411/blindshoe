import glob

for folder in ["train/labels", "valid/labels", "test/labels"]:
    for file in glob.glob(folder + "/*.txt"):

        lines = []

        with open(file, "r") as f:
            data = f.readlines()

        for line in data:
            parts = line.strip().split()

            if parts:
                if parts[0] == "23":
                    parts[0] = "7"

                lines.append(" ".join(parts) + "\n")

        with open(file, "w") as f:
            f.writelines(lines)

print("Bus class merged: ID 23 → ID 7")