from classes import User


def user_port(username, password):
    new_username = input("Enter new username: ")
    User.set_username(new_username)
