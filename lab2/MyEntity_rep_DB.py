import psycopg2
from typing import List, Optional

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
