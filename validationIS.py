    @staticmethod
    def validate_name(name: str):
        if not name or not name.isalpha():
            raise ValueError("Имя должно быть строкой и содержать только буквы.")
        return name

    @staticmethod
    def validate_comment(comment: str):
        if len(comment) > 255:
            raise ValueError("Комментарий не может превышать 255 символов.")
        return comment
