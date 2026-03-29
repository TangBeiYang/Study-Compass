from datetime import date, timedelta

from storage import load_records


def _resolve_records(records=None):
    if records is None:
        return load_records()
    return records


def _print_records(records):
    if not records:
        print("No records found.")
        return

    print()
    print(f"find {len(records)} records")
    print()
    for record in records:
        record.print_record()
        print()


def view_all_records(records=None):
    _print_records(_resolve_records(records))


def query_by_field(field_name: str, choice, records=None):
    records = _resolve_records(records)
    return [record for record in records if getattr(record, field_name, None) == choice]


def query_by_list(list_name: str, choice: list[str], records=None):
    records = _resolve_records(records)
    matched_records = []
    keywords = [item.strip().lower() for item in choice if item.strip()]
    for record in records:
        values = getattr(record, list_name, [])
        for elem in values:
            elem_text = str(elem).lower()
            if any(keyword in elem_text for keyword in keywords):
                matched_records.append(record)
                break
    return matched_records


def query_by_string(field_name: str, choice: str, records=None):
    records = _resolve_records(records)
    keyword = choice.strip().lower()
    return [record for record in records if keyword in str(getattr(record, field_name, "")).lower()]


def query_recent_x_days(x: int, records=None):
    if x <= 0:
        return []

    today = date.today()
    start_date = today - timedelta(days=x - 1)
    records = _resolve_records(records)
    matched_records = []

    for record in records:
        date_value = record.date
        if not isinstance(date_value, list) or len(date_value) != 3:
            continue
        try:
            record_date = date(date_value[0], date_value[1], date_value[2])
        except (TypeError, ValueError):
            continue

        if start_date <= record_date <= today:
            matched_records.append(record)

    return matched_records
