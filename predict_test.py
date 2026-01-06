from src.data_loader import load_csv
from src.novel_loader import load_all_novels
from pipeline import run
import csv

test = load_csv("data/test.csv")
novels = load_all_novels("data/novels")

with open("predictions.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "prediction"])

    for row in test:
        novel_key = row["book_name"].replace(" ", "_")
        novel_text = novels[novel_key]
        backstory = row["content"]

        pred = run(novel_text, backstory)
        writer.writerow([row["id"], pred])
