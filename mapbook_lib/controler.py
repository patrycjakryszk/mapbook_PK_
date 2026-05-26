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