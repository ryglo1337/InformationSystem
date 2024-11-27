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
