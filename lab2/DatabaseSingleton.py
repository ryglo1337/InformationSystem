class DatabaseSingleton:
    _instance = None

    @staticmethod
    def get_instance(db_params):
        if DatabaseSingleton._instance is None:
            DatabaseSingleton._instance = MyEntity_rep_DB(db_params)
        return DatabaseSingleton._instance
