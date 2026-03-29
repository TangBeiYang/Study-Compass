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


def _normalize_id(id_value):
    try:
        normalized = int(id_value)
        if normalized > 0:
            return normalized
    except (TypeError, ValueError):
        pass
    return None


def _next_new_id(used_ids: set[int]) -> int:
    if not used_ids:
        return 1
    return max(used_ids) + 1

def load_records():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    records = []
    used_ids = set()
    need_save = False

    for item in data:
        normalized_id = _normalize_id(item.get("id"))
        if normalized_id is None or normalized_id in used_ids:
            normalized_id = _next_new_id(used_ids)
            need_save = True
        used_ids.add(normalized_id)

        record = Record(
            id=normalized_id,
            date=_normalize_date(item.get("date")),
            category=item.get("category", ""),
            title=item.get("title", ""),
            tags=item.get("tags", []),
            status=item.get("status", ""),
            difficulty=item.get("difficulty", 1),
            blockers=item.get("blockers", []),
            note=item.get("note", ""),
        )
        records.append(record)

    if need_save:
        save_records(records)
    return records

def save_records(records):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    data = [record.to_dict() for record in records]
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def add_record(record):
    records = load_records()
    used_ids = {item.id for item in records}
    record.id = _next_new_id(used_ids)
    records.append(record)
    save_records(records)
