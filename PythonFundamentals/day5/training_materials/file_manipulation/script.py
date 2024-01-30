import json
from pathlib import Path
from datetime import datetime


def write_json(path):
    with open("hello.json", "r") as f:
        # json.dump(d, f)
        content = json.load(f)

    return content


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formatted_date = d.strftime("%d %b %Y")
    return formatted_date


if __name__ == "__main__":
    d = {"key1": "Value 1", "key2": 2, "key3": [False]}

    path = Path("hello.json")
    info = path.stat()
    print(info)

    d = convert_date(info.st_mtime)
    print(f"{path.name}\t Last Modified: {d}")
