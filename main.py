from mapbook_lib.model import users
from mapbook_lib.controler import read_users, add_user, remove_user,update_user, update_user_posts, get_user_map

def main():
    while True:
        print("===========MENU===========")
        print("0 - Zamknij program")
        print("1 - Wyświetl znajomych")
        print("2 - Dodanie znajomego")
        print("3 - Usunięcie znajomego")
        print("4 - Update znajomego")
        print("5 - Update postu znajomego")
        print("6 - Mapa lokalizacji znajomych")

        choice=input("Wybierz opcję w MENU: ")
        print(f"Wybrano eopcję {choice}")
        if choice == "0":
            break

        if choice == "1":
            read_users(users)

        if choice == "2":
            add_user(users)

        if choice == "3":
            remove_user(users)

        if choice == "4":
            update_user(users)

        if choice == "5":
            update_user_posts(users)

        if choice == "6":
            get_user_map(users)

if __name__ == "__main__":
    main()