from typing import Optional
from datetime import datetime
import json


class Client:
    def __init__(self, last_name: str, first_name: str, middle_name: Optional[str], comment: str):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__comment = comment
    
    # Методы для доступа к полям
    @property
    def last_name(self):
        return self.__last_name

    @property
    def first_name(self):
        return self.__first_name

    @property
    def middle_name(self):
        return self.__middle_name

    @property
    def comment(self):
        return self.__comment

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @middle_name.setter
    def middle_name(self, value):
        self.__middle_name = value

    @comment.setter
    def comment(self, value):
        self.__comment = value
