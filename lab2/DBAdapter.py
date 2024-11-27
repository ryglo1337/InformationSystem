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
