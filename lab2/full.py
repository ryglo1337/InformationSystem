import json
import yaml
from typing import List, Optional
from abc import ABC, abstractmethod
import psycopg2


# 1. Класс для работы с JSON - MyEntity_rep_json
class MyEntity_rep_json:
    def __init__(self, filename: str):
        self.filename = filename
        self.entities = self.read_from_file()

    def read_from_file(self) -> List[dict]:
        """Чтение всех значений из файла"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def write_to_file(self):
        """Запись всех значений в файл"""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.entities, file, ensure_ascii=False, indent=4)

    def get_by_id(self, entity_id: int) -> Optional[dict]:
        """Получить объект по ID"""
        return next((entity for entity in self.entities if entity['id'] == entity_id), None)

    def get_k_n_short_list(self, k: int, n: int) -> List[dict]:
        """Получить список k по счету n объектов класса short"""
        start = (k - 1) * n
        end = k * n
        return [entity for entity in self.entities[start:end]]

    def sort_by_field(self, field_name: str):
        """Сортировать элементы по выбранному полю"""
        self.entities.sort(key=lambda x: x.get(field_name, ''), reverse=False)

    def add_entity(self, entity: dict):
        """Добавить объект в список (при добавлении сформировать новый ID)"""
        entity['id'] = len(self.entities) + 1
        self.entities.append(entity)

    def replace_entity(self, entity_id: int, new_entity: dict):
        """Заменить элемент списка по ID"""
        for i, entity in enumerate(self.entities):
            if entity['id'] == entity_id:
                self.entities[i] = new_entity
                break

    def delete_entity(self, entity_id: int):
        """Удалить элемент списка по ID"""
        self.entities = [entity for entity in self.entities if entity['id'] != entity_id]

    def get_count(self) -> int:
        """Получить количество элементов"""
        return len(self.entities)


# 2. Класс для работы с YAML - MyEntity_rep_yaml
class MyEntity_rep_yaml:
    def __init__(self, filename: str):
        self.filename = filename
        self.entities = self.read_from_file()

    def read_from_file(self) -> List[dict]:
        """Чтение всех значений из файла"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            return []

    def write_to_file(self):
        """Запись всех значений в файл"""
        with open(self.filename, 'w', encoding='utf-8') as file:
            yaml.dump(self.entities, file, allow_unicode=True)

    def get_by_id(self, entity_id: int) -> Optional[dict]:
        """Получить объект по ID"""
        return next((entity for entity in self.entities if entity['id'] == entity_id), None)

    def get_k_n_short_list(self, k: int, n: int) -> List[dict]:
        """Получить список k по счету n объектов класса short"""
        start = (k - 1) * n
        end = k * n
        return [entity for entity in self.entities[start:end]]

    def sort_by_field(self, field_name: str):
        """Сортировать элементы по выбранному полю"""
        self.entities.sort(key=lambda x: x.get(field_name, ''), reverse=False)

    def add_entity(self, entity: dict):
        """Добавить объект в список (при добавлении сформировать новый ID)"""
        entity['id'] = len(self.entities) + 1
        self.entities.append(entity)

    def replace_entity(self, entity_id: int, new_entity: dict):
        """Заменить элемент списка по ID"""
        for i, entity in enumerate(self.entities):
            if entity['id'] == entity_id:
                self.entities[i] = new_entity
                break

    def delete_entity(self, entity_id: int):
        """Удалить элемент списка по ID"""
        self.entities = [entity for entity in self.entities if entity['id'] != entity_id]

    def get_count(self) -> int:
        """Получить количество элементов"""
        return len(self.entities)


# 3. Абстрактный класс MyEntity_rep
class MyEntity_rep(ABC):
    def __init__(self, filename: str):
        self.filename = filename

    @abstractmethod
    def read_from_file(self):
        pass

    @abstractmethod
    def write_to_file(self):
        pass

    @abstractmethod
    def get_by_id(self, entity_id: int):
        pass

    @abstractmethod
    def get_k_n_short_list(self, k: int, n: int):
        pass

    @abstractmethod
    def sort_by_field(self, field_name: str):
        pass

    @abstractmethod
    def add_entity(self, entity: dict):
        pass

    @abstractmethod
    def replace_entity(self, entity_id: int, new_entity: dict):
        pass

    @abstractmethod
    def delete_entity(self, entity_id: int):
        pass

    @abstractmethod
    def get_count(self) -> int:
        pass


# 4. Класс для работы с базой данных - MyEntity_rep_DB
class MyEntity_rep_DB:
    def __init__(self, db_params):
        self.db_params = db_params
        self.connection = psycopg2.connect(**db_params)
        self.cursor = self.connection.cursor()

    def get_by_id(self, entity_id: int) -> Optional[dict]:
        """Получить объект по ID"""
        self.cursor.execute("SELECT * FROM entities WHERE id = %s", (entity_id,))
        result = self.cursor.fetchone()
        return result

    def get_k_n_short_list(self, k: int, n: int) -> List[dict]:
        """Получить список k по счету n объектов класса short"""
        offset = (k - 1) * n
        self.cursor.execute("SELECT * FROM entities LIMIT %s OFFSET %s", (n, offset))
        return self.cursor.fetchall()

    def add_entity(self, entity: dict):
        """Добавить объект в список (при добавлении сформировать новый ID)"""
        self.cursor.execute(
            "INSERT INTO entities (name, comment) VALUES (%s, %s) RETURNING id", 
            (entity['name'], entity['comment'])
        )
        entity['id'] = self.cursor.fetchone()[0]
        self.connection.commit()

    def replace_entity(self, entity_id: int, new_entity: dict):
        """Заменить элемент списка по ID"""
        self.cursor.execute(
            "UPDATE entities SET name = %s, comment = %s WHERE id = %s", 
            (new_entity['name'], new_entity['comment'], entity_id)
        )
        self.connection.commit()

    def delete_entity(self, entity_id: int):
        """Удалить элемент списка по ID"""
        self.cursor.execute("DELETE FROM entities WHERE id = %s", (entity_id,))
        self.connection.commit()

    def get_count(self) -> int:
        """Получить количество элементов"""
        self.cursor.execute("SELECT COUNT(*) FROM entities")
        return self.cursor.fetchone()[0]


# 5. Делегирование и паттерн одиночка для работы с БД
class DatabaseSingleton:
    _instance = None

    @staticmethod
    def get_instance(db_params):
        if DatabaseSingleton._instance is None:
            DatabaseSingleton._instance = MyEntity_rep_DB(db_params)
        return DatabaseSingleton._instance


# 6. Паттерн Адаптер для работы с БД
class DBAdapter(MyEntity_rep):
    def __init__(self, db_params):
        self.db_handler = DatabaseSingleton.get_instance(db_params)

    def read_from_file(self):
        raise NotImplementedError("Этот метод не поддерживается в DBAdapter.")

    def write_to_file(self):
        raise NotImplementedError("Этот метод не поддерживается в DBAdapter.")

    def get_by_id(self, entity_id: int):
        return self.db_handler.get_by_id(entity_id)

    def get_k_n_short_list(self, k: int, n: int):
        return self.db_handler.get_k_n_short_list(k, n)

    def sort_by_field(self, field_name: str):
        raise NotImplementedError("Этот метод не поддерживается в DBAdapter.")

    def add_entity(self, entity: dict):
        return self.db_handler.add_entity(entity)

    def replace_entity(self, entity_id: int, new_entity: dict):
        return self.db_handler.replace_entity(entity_id, new_entity)

    def delete_entity(self, entity_id: int):
        return self.db_handler.delete_entity(entity_id)

    def get_count(self) -> int:
        return self.db_handler.get_count()


# 7. Паттерн Декоратор для работы с фильтрами и сортировкой для БД
class DBDecorator(MyEntity_rep_DB):
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def get_k_n_short_list(self, k: int, n: int, filter_func=None, sort_func=None):
        result = self.db_handler.get_k_n_short_list(k, n)
        if filter_func:
            result = filter(filter_func, result)
        if sort_func:
            result = sorted(result, key=sort_func)
        return result

    def get_count(self, filter_func=None):
        count = self.db_handler.get_count()
        if filter_func:
            filtered_count = sum(1 for item in range(count) if filter_func(item))
            return filtered_count
        return count


# 8. Паттерн Декоратор для работы с файлами
class FileDecorator(MyEntity_rep_json):
    def __init__(self, file_handler):
        self.file_handler = file_handler

    def get_k_n_short_list(self, k: int, n: int, filter_func=None, sort_func=None):
        result = self.file_handler.get_k_n_short_list(k, n)
        if filter_func:
            result = filter(filter_func, result)
        if sort_func:
            result = sorted(result, key=sort_func)
        return result

    def get_count(self, filter_func=None):
        count = self.file_handler.get_count()
        if filter_func:
            filtered_count = sum(1 for item in range(count) if filter_func(item))
            return filtered_count
        return count


# Пример использования:

# Использование с JSON:
json_rep = MyEntity_rep_json('data.json')
json_rep.add_entity({'name': 'Иванов Иван', 'comment': 'Регулярный клиент'})
json_rep.write_to_file()

# Использование с YAML:
yaml_rep = MyEntity_rep_yaml('data.yaml')
yaml_rep.add_entity({'name': 'Петров Петр', 'comment': 'Новый клиент'})
yaml_rep.write_to_file()

# Использование с БД:
db_params = {'dbname': 'mydb', 'user': 'user', 'password': 'password', 'host': 'localhost'}
db_rep = DBAdapter(db_params)
db_rep.add_entity({'name': 'Сидоров Сидор', 'comment': 'Очень важный клиент'})

