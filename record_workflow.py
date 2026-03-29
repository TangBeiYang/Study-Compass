from models import Record
from storage import add_record, load_records, save_records

from record_constants import CATEGORY_OPTIONS, STATUS_OPTIONS
from record_query import (
    query_by_field,
    query_by_list,
    query_by_string,
    query_recent_x_days,
    view_all_records,
)
from record_ui import (
    check_input,
    menu_date,
    menu_filter,
    menu_choose_filter,
    menu_manage_records,
    menu_main,
    menu_record_actions,
    prompt_date,
    prompt_difficulty,
    prompt_label,
    prompt_list,
    prompt_str,
)


def create_record():
    print()
    print("Create New Record")
    print("Please complete all required fields in order.")
    print()

    print("[1/4] Basic Information")
    date_input = prompt_date()
    category_input = prompt_label("Enter category:", CATEGORY_OPTIONS)
    title_input = prompt_str(
        "Enter title:",
        "Example: P1873 Cut Trees / Discrete Math - Relations",
    )

    print()
    print("[2/4] Topic and Method")
    tags_input = prompt_list(
        "Enter tags (keywords like binary-search, json, cli):",
        required=True,
    )

    print()
    print("[3/4] Completion Quality")
    status_input = prompt_label("Enter status:", STATUS_OPTIONS)
    difficulty_input = prompt_difficulty()

    print()
    print("[4/4] Reflection and Notes")
    blockers_input = prompt_list(
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


def _choose_filtered_records(records, include_back_option: bool):
    if include_back_option:
        menu_filter()
        choice = check_input(9)
        if choice == 9:
            return None, True
    else:
        menu_choose_filter()
        choice = check_input(8)

    if choice == 1:
        menu_date()
        date_choice = check_input(3)

        if date_choice == 1:
            date_chosen = prompt_date()
            return query_by_field("date", date_chosen, records), False

        if date_choice == 2:
            while True:
                print("Enter x (recent x days, including today):")
                raw = input().strip()
                try:
                    x = int(raw)
                    if x <= 0:
                        print("x must be a positive integer.")
                        continue
                    return query_recent_x_days(x, records), False
                except ValueError:
                    print("Invalid input. Please enter a positive integer.")

        return None, False

    if choice == 2:
        category_chosen = prompt_label("Enter category you choose:", CATEGORY_OPTIONS)
        return query_by_field("category", category_chosen, records), False

    if choice == 3:
        title_chosen = prompt_str("Enter title you choose:")
        return query_by_string("title", title_chosen, records), False

    if choice == 4:
        tags_chosen = prompt_list("Enter tags you choose:", required=True)
        return query_by_list("tags", tags_chosen, records), False

    if choice == 5:
        status_chosen = prompt_label("Enter status you choose:", STATUS_OPTIONS)
        return query_by_field("status", status_chosen, records), False

    if choice == 6:
        difficulty_chosen = prompt_difficulty()
        return query_by_field("difficulty", difficulty_chosen, records), False

    if choice == 7:
        blockers_chosen = prompt_list("Enter blockers you choose:", required=True)
        return query_by_list("blockers", blockers_chosen, records), False

    note_chosen = prompt_str("Enter note you choose:")
    return query_by_string("note", note_chosen, records), False


def filter_records():
    records = load_records()
    while 1:
        filtered_records, should_back = _choose_filtered_records(records, include_back_option=True)
        if should_back:
            break
        if filtered_records is None:
            continue
        view_all_records(filtered_records)


def _view_selected_record(records, record_id: int):
    found = False
    for record in records:
        if record.id == record_id:
            record.print_record()
            found = True
            break
    if not found:
        print(f"No record found with id {record_id}.")


def _edit_selected_record(records, record_id: int):
    index = None
    for i in range(len(records)):
        if records[i].id == record_id:
            index = i
            break
    if index is None:
        print(f"No record found with id {record_id}.")
        return records

    print()
    print("Change Record")
    print("Please complete all required fields in order.")
    print()

    print("[1/4] Basic Information")
    date_input = prompt_date()
    category_input = prompt_label("Enter category:", CATEGORY_OPTIONS)
    title_input = prompt_str(
        "Enter title:",
        "Example: P1873 Cut Trees / Discrete Math - Relations",
    )

    print()
    print("[2/4] Topic and Method")
    tags_input = prompt_list(
        "Enter tags (keywords like binary-search, json, cli):",
        required=True,
    )

    print()
    print("[3/4] Completion Quality")
    status_input = prompt_label("Enter status:", STATUS_OPTIONS)
    difficulty_input = prompt_difficulty()

    print()
    print("[4/4] Reflection and Notes")
    blockers_input = prompt_list(
        "Enter blockers (what exactly blocked you). Leave empty if none:",
        required=(status_input == "stuck"),
    )

    print("Enter note (optional, press Enter to skip):")
    note_input = input().strip()

    id_pre = records[index].id
    records[index] = Record(
        id=id_pre,
        date=date_input,
        category=category_input,
        title=title_input,
        tags=tags_input,
        status=status_input,
        difficulty=difficulty_input,
        blockers=blockers_input,
        note=note_input,
    )
    save_records(records)
    print("Record changed successfully.")
    return records


def _delete_selected_record(records, record_id: int):
    deleted = False
    for record in records:
        if record.id == record_id:
            records.remove(record)
            deleted = True
            break
    if not deleted:
        print(f"No record found with id {record_id}.")
        return records
    save_records(records)
    print("Delete record successfully.")
    return records


def _record_actions_menu_loop(records, allowed_ids=None):
    while 1:
        menu_record_actions()
        choice = check_input(4)

        if choice != 4:
            while True:
                print("Enter id you choose:")
                raw = input().strip()
                try:
                    id_input = int(raw)
                    if id_input <= 0:
                        print("id must be a positive integer.")
                        continue
                    if allowed_ids is not None and id_input not in allowed_ids:
                        print("This id is not in current filtered results.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a positive integer.")

        if choice == 1:
            _view_selected_record(records, id_input)

        elif choice == 2:
            records = _edit_selected_record(records, id_input)

        elif choice == 3:
            records = _delete_selected_record(records, id_input)
            if allowed_ids is not None:
                allowed_ids.discard(id_input)

        elif choice == 4:
            break


def choose_from_all_records(records):
    print()
    view_all_records(records)
    _record_actions_menu_loop(records)


def choose_from_filtered_results(records):
    print()
    filtered_records, _ = _choose_filtered_records(records, include_back_option=False)
    if filtered_records is None:
        return

    view_all_records(filtered_records)
    if not filtered_records:
        return

    allowed_ids = {record.id for record in filtered_records}
    _record_actions_menu_loop(records, allowed_ids)


def manage_records():
    records = load_records()
    while 1:
        menu_manage_records()
        choice = check_input(3)

        if choice == 1:
            choose_from_all_records(records)

        elif choice == 2:
            choose_from_filtered_results(records)

        elif choice == 3:
            break
