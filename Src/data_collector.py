import csv
import os
from datetime import datetime, timezone


DATA_FILE = "data/raw/market_data.csv"


def save_candle(timestamp, open_price, high, low, close, volume):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    file_exists = os.path.isfile(DATA_FILE)

    with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "open",
                "high",
                "low",
                "close",
                "volume"
            ])

        writer.writerow([
            timestamp,
            open_price,
            high,
            low,
            close,
            volume
        ])


def create_test_candle():
    timestamp = datetime.now(timezone.utc).isoformat()

    save_candle(
        timestamp,
        100.0,
        101.0,
        99.0,
        100.5,
        1000
    )


if __name__ == "__main__":
    create_test_candle()
    print("Test market data saved successfully.")
