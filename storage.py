import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

def load_data(filename, default):
    path = DATA_DIR / filename
    if not path.exists():
        save_data(filename, default)
        return default
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return default

def save_data(filename, data):
    path = DATA_DIR / filename
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
