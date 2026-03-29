import record_workflow

while 1:
    record_workflow.menu_main()

    choice = record_workflow.check_input(5)

    if choice == 1:
        record_workflow.create_record()

    elif choice == 2:
        record_workflow.view_all_records()

    elif choice == 3:
        record_workflow.filter_records()

    elif choice == 4:
        record_workflow.manage_records()

    elif choice == 5:
        break
