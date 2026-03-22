import record_workflow

while 1:
    record_workflow.menu_main()

    choice = record_workflow.check_input(4)

    if choice == 1:
        record_workflow.create_record()

    elif choice == 2:
        record_workflow.view_all_records()

    elif choice == 3:
        record_workflow.filter_records()

    elif choice == 4:
        break

    else:
        print()
        print("Invalid input. Please enter an integer between 1 and 4.")

