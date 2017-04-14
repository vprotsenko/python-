import front_part as front
import backend_part as back


def start_screen():
    back.sync_var()

    app_status = True
    while app_status:
        choice = input("\"l\" to login \n"
                       "\"r\" for registration \n"
                       "\"e\" for exit \n")
        if choice == 'r':
            front.registration()
            app_status = front.login()
        elif choice == 'l':
            app_status = front.login()
        elif choice == 'e':
            app_status = front.login()
        else:
            app_status = True

    back.dump_var_to_db()


start_screen()