from abc import ABC, abstractmethod

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
