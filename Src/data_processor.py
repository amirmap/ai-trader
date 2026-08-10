import csv
import os


RAW_FILE = "data/raw/market_data.csv"
PROCESSED_FILE = "data/processed/market_data.csv"


def process_market_data():
    if not os.path.isfile(RAW_FILE):
        print("Raw market data file not found.")
        return

    os.makedirs(os.path.dirname(PROCESSED_FILE), exist_ok=True)

    with open(RAW_FILE, "r", newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        rows = list(reader)

    if not rows:
        print("No market data available.")
        return

    with open(PROCESSED_FILE, "w", newline="", encoding="utf-8") as target:
        fieldnames = [
            "timestamp",
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]

        writer = csv.DictWriter(target, fieldnames=fieldnames)
        writer.writeheader()

        for row in rows:
            writer.writerow(row)

    print("Market data processed successfully.")


if __name__ == "__main__":
    process_market_data()
