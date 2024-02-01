import json
from datetime import datetime


class User:
    def __init__(self, first_name: str, last_name: str, username: str, password: str, course_list: list, status="0"):
        self.first_name = first_name
        self.last_name = last_name
        self.__username = username
        self.__password = password
        self.course_list = course_list
        self.__status = status
        self.__created_date = datetime.now()

    @staticmethod
    def get_username(self):
        return self.__username

    @staticmethod
    def set_username(self, new_username: str):
        with open("users.json", "r") as file:
            data = json.load(file)
        for user in data["users"]:
            while user["username"] == new_username:
                print("This username already used!")
                new_username = input("Enter new username: ")
        self.__username = new_username
        return "Successful"
