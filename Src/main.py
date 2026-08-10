from config import APP_NAME, VERSION, ENVIRONMENT


def start():
    print("=" * 40)
    print(APP_NAME)
    print(f"Version: {VERSION}")
    print(f"Environment: {ENVIRONMENT}")
    print("System started successfully.")
    print("=" * 40)


if __name__ == "__main__":
    start()
