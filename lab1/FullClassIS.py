import json
from typing import Optional

# 1. Определяем класс Client с инкапсуляцией полей
class Client:
    def __init__(self, last_name: str, first_name: str, middle_name: Optional[str] = None, comment: str = ""):
        self.__last_name = self.validate_name(last_name)
        self.__first_name = self.validate_name(first_name)
        self.__middle_name = middle_name
        self.__comment = self.validate_comment(comment)

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
        self.__last_name = self.validate_name(value)

    @first_name.setter
    def first_name(self, value):
        self.__first_name = self.validate_name(value)

    @middle_name.setter
    def middle_name(self, value):
        self.__middle_name = value

    @comment.setter
    def comment(self, value):
        self.__comment = self.validate_comment(value)

    # Статические методы для валидации данных
    @staticmethod
    def validate_string(value: str, field_name: str, max_length: int = 255):
        if not value or not isinstance(value, str):
            raise ValueError(f"{field_name} должно быть строкой.")
        if len(value) > max_length:
            raise ValueError(f"{field_name} не может быть длиннее {max_length} символов.")
        return value

    @staticmethod
    def validate_name(name: str):
        return Client.validate_string(name, "Имя", 50)

    @staticmethod
    def validate_comment(comment: str):
        return Client.validate_string(comment, "Комментарий", 255)

    # Перегрузка конструктора для создания объекта из JSON
    @classmethod
    def from_json(cls, json_data: str):
        data = json.loads(json_data)
        return cls(
            last_name=data["last_name"],
            first_name=data["first_name"],
            middle_name=data.get("middle_name"),
            comment=data.get("comment", "")
        )

    # Методы для вывода информации
    def full_info(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}, {self.comment}"

    def short_info(self):
        return f"{self.last_name} {self.first_name[0]}."

# 2. Класс для краткой версии данных (наследование от Client)
class ShortClient(Client):
    def full_info(self):
        raise NotImplementedError("Полная информация недоступна для краткой версии.")
    
    def short_info(self):
        return f"{self.last_name} {self.first_name[0]}."

# Пример использования:
if __name__ == "__main__":
    # Создание объекта клиента
    client_data = {
        "last_name": "Иванов",
        "first_name": "Иван",
        "middle_name": "Иванович",
        "comment": "Регулярный клиент"
    }

    # Создание клиента с использованием конструктора
    client = Client(**client_data)
    print(client.full_info())  # Полная информация
    print(client.short_info())  # Краткая информация

    # Создание клиента из JSON строки
    json_data = '{"last_name": "Петров", "first_name": "Петр", "middle_name": "Петрович", "comment": "Новый клиент"}'
    new_client = Client.from_json(json_data)
    print(new_client.full_info())  # Полная информация
    print(new_client.short_info())  # Краткая информация

    # Создание краткой версии клиента
    short_client = ShortClient(**client_data)
    print(short_client.short_info())  # Краткая информация (без полной)
