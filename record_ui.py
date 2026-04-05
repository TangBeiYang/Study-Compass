from datetime import datetime, date

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


def menu_edit_action():
    print()
    print("Edit actions")
    print("1. Edit date")
    print("2. Edit category")
    print("3. Edit title")
    print("4. Edit tags")
    print("5. Edit status")
    print("6. Edit difficulty")
    print("7. Edit blockers")
    print("8. Edit note")
    print("9. Edit all")
    print("10. Back")
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


def prompt_str(
    prompt_text: str,
    example: str = "",
    keep_value: str | None = None,
    edit: bool = False,
    allow_empty: bool = False,
) -> str:
    while True:
        print(prompt_text)
        if example:
            print(example)
        if edit:
            print("Enter & to keep the original value.")
        value = input().strip()
        if edit and value == "&":
            result = keep_value if keep_value is not None else ""
            print(f"Saved: {result if result else '(empty)'}")
            return result
        if value:
            print(f"Saved: {value}")
            return value
        if allow_empty:
            print("Saved: (empty)")
            return ""
        if edit:
            print("Input cannot be empty. Please enter text or &.")
        else:
            print("Input cannot be empty. Please try again.")


def prompt_date(keep_value: list[int] | None = None, edit: bool = False) -> list[int]:
    while True:
        print("Enter date in YYYY-MM-DD format (example: 2026-03-15).")
        print("Press Enter directly to use today's date.")
        print("Date will be stored as [year, month, day].")
        if edit:
            print("Enter & to keep the original value.")
        value = input().strip()
        try:
            if edit and value == "&":
                result = keep_value[:]
                print(f"Saved date: {result[0]:04d}-{result[1]:02d}-{result[2]:02d}")
                return result
            if value == "":
                today = date.today()
                result = [today.year, today.month, today.day]
                print(f"Saved date: {result[0]:04d}-{result[1]:02d}-{result[2]:02d}")
                return result
            parsed = datetime.strptime(value, "%Y-%m-%d")
            result = [parsed.year, parsed.month, parsed.day]
            print(f"Saved date: {result[0]:04d}-{result[1]:02d}-{result[2]:02d}")
            return result
        except ValueError:
            if edit:
                print("Invalid date format. Please use YYYY-MM-DD, Enter, or &.")
            else:
                print("Invalid date format. Please use YYYY-MM-DD or press Enter.")


def prompt_label(
    prompt_text: str,
    options: list[str],
    keep_value: list[str] | None = None,
    edit: bool = False,
) -> str:
    allowed = {item.lower(): item for item in options}
    while True:
        print(prompt_text)
        print(f"Allowed values: {', '.join(options)}")
        if edit:
            print("Enter & to keep the original value.")
        value = input().strip().lower()
        if edit and value == "&":
            print(f"Saved: {keep_value}")
            return keep_value
        if value in allowed:
            result = allowed[value]
            print(f"Saved: {result}")
            return result
        if edit:
            print("Invalid choice. Please select one of the allowed values or enter &.")
        else:
            print("Invalid choice. Please select one of the allowed values.")


def prompt_category(
    category_options: list[str],
    keep_value: str | None = None,
    edit: bool = False,
) -> str:
    allowed = {item.lower(): item for item in category_options}
    shortcut_map = {
        "p": "problem",
        "c": "course",
        "pj": "project",
        "r": "research",
    }

    while True:
        print("Enter category by full name or shortcut.")
        print(f"Allowed values: {', '.join(category_options)}")
        print("Shortcuts: p=problem, c=course, pj=project, r=research")
        if edit:
            print("Enter & to keep the original value.")

        value = input().strip().lower()
        if edit and value == "&":
            result = keep_value if keep_value is not None else ""
            print(f"Saved: {result}")
            return result

        if value in allowed:
            result = allowed[value]
            print(f"Saved: {result}")
            return result

        if value in shortcut_map:
            result = shortcut_map[value]
            print(f"Saved: {result}")
            return result

        if edit:
            print("Invalid choice. Use allowed values, shortcuts, or &.")
        else:
            print("Invalid choice. Use allowed values or shortcuts.")


def prompt_list(
    prompt_text: str,
    required: bool = False,
    keep_value: list[str] | None = None,
    edit: bool = False,
) -> list[str]:
    while True:
        print(prompt_text)
        print("Use commas to separate multiple items.")
        if edit:
            print("Enter & to keep the original value.")
        raw = input().strip().replace("，", ",")
        if edit and raw == "&":
            result = keep_value[:] if keep_value is not None else []
            print(f"Saved: {', '.join(result) if result else '(empty)'}")
            return result

        if not raw:
            if required:
                print("At least one item is required.")
                continue
            print("Saved: (empty)")
            return []

        items = []
        for item in raw.split(","):
            cleaned = item.strip()
            if cleaned and cleaned not in items:
                items.append(cleaned)

        if required and not items:
            print("At least one valid item is required.")
            continue
        print(f"Saved: {', '.join(items)}")
        return items


def prompt_difficulty(keep_value: int | None = None, edit: bool = False) -> int:
    while True:
        print("Enter difficulty from 1 to 6 (1 = easy, 6 = hard):")
        if edit:
            print("Enter & to keep the original value.")
        raw = input().strip()
        if edit and raw == "&":
            result = keep_value if keep_value is not None else 1
            print(f"Saved: {result}")
            return result
        try:
            value = int(raw)
            if 1 <= value <= 6:
                print(f"Saved: {value}")
                return value
            print("Difficulty must be between 1 and 6.")
        except ValueError:
            if edit:
                print("Invalid input. Please enter 1-6 or &.")
            else:
                print("Invalid input. Please enter an integer between 1 and 6.")
