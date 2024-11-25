  @staticmethod
    def validate_string(value: str, field_name: str, max_length: int = 255):
        if not value or not isinstance(value, str):
            raise ValueError(f"{field_name} должно быть строкой.")
        if len(value) > max_length:
            raise ValueError(f"{field_name} не может быть длиннее {max_length} символов.")
        return value
