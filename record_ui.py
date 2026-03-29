from datetime import datetime


def menu_main():
    print()
    print("1. Add one record")
    print("2. View all records")
    print("3. Filter records")
    print("4. Manage records")
    print("5. Exit")
    print("Please enter your choice:")


def menu_filter():
    print()
    print("1. View by date")
    print("2. View by category")
    print("3. View by title")
    print("4. View by tag")
    print("5. View by status")
    print("6. View by difficulty")
    print("7. View by blocker")
    print("8. View by note")
    print("9. Back")
    print("Please enter your choice:")


def menu_choose_filter():
    print()
    print("1. View by date")
    print("2. View by category")
    print("3. View by title")
    print("4. View by tag")
    print("5. View by status")
    print("6. View by difficulty")
    print("7. View by blocker")
    print("8. View by note")
    print("Please enter your choice:")


def menu_date():
    print()
    print("1. View by exact day")
    print("2. View recent x days")
    print("3. Back")
    print("Please enter your choice:")


def menu_manage_records():
    print()
    print("Manage records")
    print("1. Choose from all records")
    print("2. Choose from filtered results")
    print("3. Back")
    print("Please enter your choice:")


def menu_record_actions():
    print()
    print("Record actions:")
    print("1. View this record")
    print("2. Edit this record")
    print("3. Delete this record")
    print("4. Back")
    print("Please enter your choice:")


def check_input(num: int):
    while True:
        choice_raw = input().strip()
        try:
            choice_input = int(choice_raw)
            if choice_input > num or choice_input < 1:
                print(f"Invalid input. Please enter an integer between 1 and {num}.")
                continue
            break
        except ValueError:
            print(f"Invalid input. Please enter an integer between 1 and {num}.")
    return choice_input


def prompt_str(prompt_text: str, example: str = "") -> str:
    while True:
        print(prompt_text)
        if example:
            print(example)
        value = input().strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def prompt_date() -> list[int]:
    while True:
        print("Enter date in YYYY-MM-DD format (example: 2026-03-15).")
        print("It will be stored as [year, month, day].")
        value = input().strip()
        try:
            parsed = datetime.strptime(value, "%Y-%m-%d")
            return [parsed.year, parsed.month, parsed.day]
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def prompt_label(prompt_text: str, options: list[str]) -> str:
    allowed = {item.lower(): item for item in options}
    while True:
        print(prompt_text)
        print(f"Allowed values: {', '.join(options)}")
        value = input().strip().lower()
        if value in allowed:
            return allowed[value]
        print("Invalid choice. Please select one of the allowed values.")


def prompt_list(prompt_text: str, required: bool = False) -> list[str]:
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


def prompt_difficulty() -> int:
    while True:
        print("Enter difficulty from 1 to 6 (1 = easy, 6 = hard):")
        raw = input().strip()
        try:
            value = int(raw)
            if 1 <= value <= 6:
                return value
            print("Difficulty must be between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 6.")
