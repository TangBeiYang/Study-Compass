from models import Record
from storage import save_records

from record_constants import CATEGORY_OPTIONS, STATUS_OPTIONS
from record_ui import (
    prompt_date,
    prompt_difficulty,
    prompt_category,
    prompt_label,
    prompt_list,
    prompt_str,
)


def _edit_record_all(records, index: int):
    print()
    print("Change Record")
    print("Please complete all required fields in order.")
    print()

    print("[1/4] Basic Information")
    date_input = prompt_date(records[index].date, True)
    category_input = prompt_category(CATEGORY_OPTIONS, records[index].category, True)
    title_input = prompt_str(
        "Enter title:",
        "Example: P1873 Cut Trees / Discrete Math - Relations",
        records[index].title,
        True,
    )

    print()
    print("[2/4] Topic and Method")
    tags_input = prompt_list(
        "Enter tags (keywords like binary-search, json, cli):",
        required=True,
        keep_value=records[index].tags,
        edit=True,
    )

    print()
    print("[3/4] Completion Quality")
    status_input = prompt_label("Enter status:", STATUS_OPTIONS, records[index].status, True)
    difficulty_input = prompt_difficulty(records[index].difficulty, True)

    print()
    print("[4/4] Reflection and Notes")
    blockers_input = prompt_list(
        "Enter blockers (what exactly blocked you). Leave empty if none:",
        required=(status_input == "stuck"),
        keep_value=records[index].blockers,
        edit=True,
    )

    note_input = prompt_str(
        "Enter note (optional, press Enter to skip):",
        keep_value=records[index].note,
        edit=True,
        allow_empty=True,
    )

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


def _edit_record_date(records, index: int):
    date_input = prompt_date(records[index].date, True)
    records[index].date = date_input
    save_records(records)
    print("Record changed successfully.")
    return records


def _edit_record_category(records, index: int):
    category_input = prompt_category(CATEGORY_OPTIONS, records[index].category, True)
    records[index].category = category_input
    save_records(records)
    print("Record changed successfully.")
    return records


def _edit_record_title(records, index: int):
    title_input = prompt_str(
        "Enter title:",
        "Example: P1873 Cut Trees / Discrete Math - Relations",
        records[index].title,
        True,
    )
    records[index].title = title_input
    save_records(records)
    print("Record changed successfully.")
    return records


def _edit_record_tags(records, index: int):
    tags_input = prompt_list(
        "Enter tags (keywords like binary-search, json, cli):",
        required=True,
        keep_value=records[index].tags,
        edit=True,
    )
    records[index].tags = tags_input
    save_records(records)
    print("Record changed successfully.")
    return records


def _edit_record_status(records, index: int):
    status_input = prompt_label("Enter status:", STATUS_OPTIONS, records[index].status, True)
    records[index].status = status_input
    save_records(records)
    print("Record changed successfully.")
    return records


def _edit_record_difficulty(records, index: int):
    difficulty_input = prompt_difficulty(records[index].difficulty, True)
    records[index].difficulty = difficulty_input
    save_records(records)
    print("Record changed successfully.")
    return records


def _edit_record_blockers(records, index: int):
    blockers_input = prompt_list(
        "Enter blockers (what exactly blocked you). Leave empty if none:",
        required=(records[index].status == "stuck"),
        keep_value=records[index].blockers,
        edit=True,
    )
    records[index].blockers = blockers_input
    save_records(records)
    print("Record changed successfully.")
    return records


def _edit_record_note(records, index: int):
    note_input = prompt_str(
        "Enter note (optional, press Enter to skip):",
        keep_value=records[index].note,
        edit=True,
        allow_empty=True,
    )
    records[index].note = note_input
    save_records(records)
    print("Record changed successfully.")
    return records
