import sys
import requests
from pathlib import Path


def make_request(url, file):
    headers = {
        "Content-Type": "application/soap+xml; charset=utf-8",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.12.5",
    }
    
    file_path = Path(file)
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        
            response = requests.post(url, headers=headers, data=content)
            if response:
                print(f"Response from server:\n{response.text}")
        
    else:
        print("File not found.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("How to use: python3 send_soap.py <url> <file>\n")
        sys.exit(1)

    make_request(sys.argv[1], sys.argv[2])

