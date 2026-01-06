import os

def load_all_novels(novel_dir):
    novels = {}
    for file in os.listdir(novel_dir):
        key = file.replace(".txt", "").replace(" ", "_")
        with open(os.path.join(novel_dir, file), encoding="utf-8") as f:
            novels[key] = f.read()
    return novels
