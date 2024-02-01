import json
from user_port import user_port
from admin_port import admin_port


def main():
    username = input("username: ")
    password = input("password: ")
    with open("users.json", "r") as file:
        data = json.load(file)
    for user in data["users"]:
        if user["username"] == username and user["password"]:
            if user["status"] == '0':
                return user_port(username, password)
            else:
                return admin_port(username, password)
    choice = input("Do you want to sign up? yes/no\n>>> ")
    while choice != 'yes' and choice != 'no':
        choice = input('''
Command not found!
Do you want to sign up? yes/no\n>>> ''')
    if choice == "no":
        return main()
    else:
        pass


if __name__ == "__main__":
    print(main())
