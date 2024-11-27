import yaml
from typing import List, Optional

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
