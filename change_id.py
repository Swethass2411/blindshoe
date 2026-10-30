from pathlib import Path

folders = [
    r"C:\Users\SwethaS\Downloads\Person Person Person.v1i.yolov8\train\labels",
    r"C:\Users\SwethaS\Downloads\Person Person Person.v1i.yolov8\valid\labels",
    r"C:\Users\SwethaS\Downloads\Person Person Person.v1i.yolov8\test\labels"
]

for folder in folders:
    for file in Path(folder).glob("*.txt"):
        lines = file.read_text().splitlines()
        new_lines = []
        for line in lines:
            parts = line.split()
            if parts and parts[0] == "0":
                parts[0] = "13"   # person class ID in your Combined_Dataset
            new_lines.append(" ".join(parts))
        file.write_text("\n".join(new_lines))

print("Done! Person labels changed from 0 to 13.")