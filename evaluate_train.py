from src.data_loader import load_csv
from src.novel_loader import load_all_novels
from pipeline import run

train = load_csv("data/train.csv")
novels = load_all_novels("data/novels")

correct = 0
errors = 0

for row in train:
    try:
        novel_key = row["book_name"].replace(" ", "_")
        novel_text = novels[novel_key]

        backstory = row["content"]
        label = row["label"].lower()

        pred = run(novel_text, backstory)
        gold = 1 if label == "consistent" else 0

        correct += int(pred == gold)

    except KeyError as e:
        errors += 1
        print("Missing column:", e)

print("Train accuracy:", correct / (len(train) - errors))
print("Rows skipped:", errors)

