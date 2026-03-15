from datetime import datetime

from models import Record
from storage import add_record, load_records


def menu():
    print()
    print("1. Add one record")
    print("2. View all records")
    print("3. Exit")
    print("Please enter your choice:")


def check_input():
    while True:
        choice_raw = input().strip()
        try:
            choice_input = int(choice_raw)
            break
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3):")
    return choice_input


def _prompt_str(prompt_text: str, example: str = "") -> str:
    while True:
        print(prompt_text)
        if example:
            print(example)
        value = input().strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def _prompt_date() -> list[int]:
    while True:
        print("Enter date in YYYY-MM-DD format (example: 2026-03-15).")
        print("It will be stored as [year, month, day].")
        value = input().strip()
        try:
            parsed = datetime.strptime(value, "%Y-%m-%d")
            return [parsed.year, parsed.month, parsed.day]
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def _prompt_label(prompt_text: str, options: list[str]) -> str:
    allowed = {item.lower(): item for item in options}
    while True:
        print(prompt_text)
        print(f"Allowed values: {', '.join(options)}")
        value = input().strip().lower()
        if value in allowed:
            return allowed[value]
        print("Invalid choice. Please select one of the allowed values.")


def _prompt_list(prompt_text: str, required: bool = False) -> list[str]:
    while True:
        print(prompt_text)
        print("Use commas to separate multiple items.")
        raw = input().strip().replace("，", ",")

        if not raw:
            if required:
                print("At least one item is required.")
                continue
            return []

        items = []
        for item in raw.split(","):
            cleaned = item.strip()
            if cleaned and cleaned not in items:
                items.append(cleaned)

        if required and not items:
            print("At least one valid item is required.")
            continue
        return items


def _prompt_difficulty() -> int:
    while True:
        print("Enter difficulty from 1 to 5 (1 = easy, 5 = hard):")
        raw = input().strip()
        try:
            value = int(raw)
            if 1 <= value <= 5:
                return value
            print("Difficulty must be between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 5.")


def create_record():
    print()
    print("Create New Record")
    print("Please complete all required fields in order.")
    print()

    print("[1/4] Basic Information")
    date_input = _prompt_date()
    category_input = _prompt_label(
        "Enter category:",
        ["problem", "course", "project"],
    )
    title_input = _prompt_str(
        "Enter title:",
        "Example: P1873 Cut Trees / Discrete Math - Relations",
    )

    print()
    print("[2/4] Topic and Method")
    tags_input = _prompt_list(
        "Enter tags (keywords like binary-search, json, cli):",
        required=True,
    )

    print()
    print("[3/4] Completion Quality")
    status_input = _prompt_label(
        "Enter status:",
        ["solved", "hinted", "stuck"],
    )
    difficulty_input = _prompt_difficulty()

    print()
    print("[4/4] Reflection and Notes")
    blockers_input = _prompt_list(
        "Enter blockers (what exactly blocked you). Leave empty if none:",
        required=(status_input == "stuck"),
    )

    print("Enter note (optional, press Enter to skip):")
    note_input = input().strip()

    record = Record(
        date=date_input,
        category=category_input,
        title=title_input,
        tags=tags_input,
        status=status_input,
        difficulty=difficulty_input,
        blockers=blockers_input,
        note=note_input,
    )

    add_record(record)
    print("Record added successfully.")


def view_all_records():
    records = load_records()

    if not records:
        print("No records found.")
        return

    print()
    for record in records:
        record.print_record()
        print()
