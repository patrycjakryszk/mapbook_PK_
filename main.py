# definicja prostej struktury danych obejmującej przykładowego użytkownika

users = [
    {"name": "Patrycja", "location": "Krasnosielc",
     "posts": ["Sprzedam mercedesa", "Kupie skrzynie biegów", "Kto idzie dzisiaj biegać?"]},
    {"name": "Alicja", "location": "Bugzy Płońskie",
     "posts": ["Mój kod nie działa pomocy!!"]},
    {"name": "Oliwia", "location": "Uciekajka",
     "posts": ["Czy ktos zrobił już sprawozdanie PPyt?"]}

]


def read_users(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user['name']} z miejscowości {user['location']} opublikował post {user['posts'][-1]}")


def add_user(users_data: list) -> None:
    users_data.append({"name": input("Podaj imie uzytkownika: "), "location": input("Podaj swoja lokalizacje: "),
                       "posts": ["Dołączono do znajomych"]})


def remove_user(users_data: list) -> None:
    user_to_remove = input("Podaj imie znajmowego do usunięcia: ")
    for user in users_data:
        if user["name"] == user_to_remove:
            users.remove(user)

def update_user(users_data: list) -> None:
    user_to_update = input("Podaj imie znajmowego do update'u: ")
    for user in users_data:
        if user["name"] == user_to_update:
            user["name"] = input("Podaj nowe imie użytkownika: ")
            user["location"] = input("Podaj nową lokalizację: ")

def update_user_posts(users_data: list) -> None:
    user_to_update = input("Podaj imie znajmowego do update'u: ")
    for user in users_data:
        if user["name"] == user_to_update:
            user["posts"].append(input("Co słychać?: "))

while True:
    print("===========MENU===========")
    print("0 - zamknij program")
    print("1 - wyświetl znajomych")
    print("2 - dodanie znajomego")
    print("3 - usunięcie znajomego")
    print("4 - Update znajomego")
    print("5 - Update postu znajomego")

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