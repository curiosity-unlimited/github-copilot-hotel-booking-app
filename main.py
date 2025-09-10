import os
from dotenv import load_dotenv

load_dotenv()
secret_key = os.getenv("SECRET_KEY")


def main():
    print("Hello from github-copilot-hotel-booking-app!")


if __name__ == "__main__":
    main()
