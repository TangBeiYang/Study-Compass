import json
from models import Record
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("data/record.json")


def _normalize_date(date_value) -> list[int]:
    if isinstance(date_value, list) and len(date_value) == 3:
        try:
            y, m, d = [int(v) for v in date_value]
            datetime(year=y, month=m, day=d)
            return [y, m, d]
        except (ValueError, TypeError):
            return [1970, 1, 1]

    if isinstance(date_value, str):
        try:
            parsed = datetime.strptime(date_value, "%Y-%m-%d")
            return [parsed.year, parsed.month, parsed.day]
        except ValueError:
            return [1970, 1, 1]

    return [1970, 1, 1]

def load_records():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    records=[]
    for item in data:
        record=Record(
            date=_normalize_date(item.get("date")),
            category=item["category"],
            title=item["title"],
            tags=item["tags"],
            status=item["status"],
            difficulty=item["difficulty"],
            blockers=item["blockers"],
            note=item["note"]
        )
        records.append(record)
    return records

def save_records(records):
    data = [record.to_dict() for record in records]
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def add_record(record):
    records = load_records()
    records.append(record)
    save_records(records)
