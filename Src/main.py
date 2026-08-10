from config import APP_NAME, VERSION, ENVIRONMENT
from data_collector import create_test_candle
from data_processor import process_market_data


def start():
    print("=" * 40)
    print(APP_NAME)
    print(f"Version: {VERSION}")
    print(f"Environment: {ENVIRONMENT}")
    print("=" * 40)

    print("Collecting market data...")
    create_test_candle()

    print("Processing market data...")
    process_market_data()

    print("AI Trader started successfully.")


if __name__ == "__main__":
    start()
