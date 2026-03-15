import record_workflow

while 1:
    record_workflow.menu()

    choice = record_workflow.check_input()

    if choice == 1:
        record_workflow.create_record()

    elif choice == 2:
        record_workflow.view_all_records()

    elif choice == 3:
        break

    else:
        print()
        print("Input Error!")

