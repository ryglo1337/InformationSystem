import json

class Client:
    def init(self, last_name, first_name, middle_name, comment):
        # Используем сеттеры для установки значений
        self.last_name = self.validate_value(last_name, "Last name", is_required=True, only_letters=True)
        self.first_name = self.validate_value(first_name, "First name", is_required=True, only_letters=True)
        self.middle_name = self.validate_value(middle_name, "Middle name", is_required=False, only_letters=True)
        self.comment = self.validate_value(comment, "Сomment", is_required=True, only_letters_and_spaces=True)
        

    
     def validate_value(value, field_name, is_required=True, only_letters=False, only_letters_and_spaces=False):
        """
        Универсальный метод валидации.
        """
        if is_required and not value.strip():
            raise ValueError(f"{field_name} cannot be empty.")
        
        if only_letters and not value.replace(' ', '').isalpha():
            raise ValueError(f"{field_name} must contain only letters.")
        
        if only_letters_and_spaces and not all(char.isalpha() or char.isspace() for char in value):
            raise ValueError(f"{field_name} must contain only letters and spaces.")
    
    @classmethod
    def from_string(cls, data_string, delimiter=","):
        """
        Создает экземпляр из строки, где значения разделены заданным разделителем.
        """
        fields = data_string.split(delimiter)
        if len(fields) != 8:
            raise ValueError("Data string must contain exactly 8 fields separated by the delimiter.")
        
        validated_fields = [
            cls.validate_value(field.strip(), field_name, **validation_rules)
            for field, (field_name, validation_rules) in zip(fields, [
                ("Last name", {"is_required": True, "only_letters": True}),
                ("First name", {"is_required": True, "only_letters": True}),
                ("Middle name", {"is_required": False, "only_letters": True}),
                ("Comment", {"is_required": True, "only_letters_and_spaces": True}),
            ])
        ]
        
        return cls(*validated_fields)
    @classmethod
    def from_json(cls, json_string):
        """
        Создает экземпляр из JSON-строки.
        """
        try:
            data = json.loads(json_string)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {e}")
        
        required_keys = [
            ("last_name", "Last name", {"is_required": True, "only_letters": True}),
            ("first_name", "First name", {"is_required": True, "only_letters": True}),
            ("middle_name", "Middle name", {"is_required": False, "only_letters": True}),
            ("comment", "Comment", {"is_required": True, "only_letters_and_spaces": True}),
        ]
        
        validated_data = {
            key: cls.validate_value(data.get(key, "").strip(), field_name, **validation_rules)
            for key, field_name, validation_rules in required_keys
        }
        
        return cls(
            last_name=validated_data["last_name"],
            first_name=validated_data["first_name"],
            middle_name=validated_data["middle_name"],
            comment=validated_data["comment"],
        )

    def str(self):
        return (
            f"Full Details:\n"
            f"Last Name: {self.last_name}\n"
            f"First Name: {self.first_name}\n"
            f"Middle Name: {self.middle_name}\n"
            f"Comment: {self.comment}\n"
           
        )
    # Вывод краткой версии объекта
    def repr(self):
        return f"Client({self.first_name} {self.last_name}, {self.profession})"
    # Сравнение объектов на равенство
    def eq(self, other):
        if not isinstance(other, Client):
            return NotImplemented
        return (
            self.last_name == other.last_name and
            self.first_name == other.first_name and
            self.middle_name == other.middle_name and
            self.comment == other.comment
        )


    # Геттеры
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
    def qualification(self):
        return self.__comment
   
    # Сеттеры
    @last_name.setter
    def last_name(self, value):
        self.__last_name = value
    @first_name.setter
    def first_name(self, value):
        self.__first_name = value
    @middle_name.setter
    def middle_name(self, value):
        self.__middle_name = value
    @comment.setter
    def qualification(self, value):
        self.__comment = value

  class ShortClient:
    def init(self, client):
        if not isinstance(client, Client):
            raise ValueError("Expected an instance of Client.")
        self._base = client  # Храним ссылку на базовый объект
    @property
    def first_name(self):
        return self._base.first_name  # Делегируем доступ
    @property
    def last_name(self):
        return self._base.last_name  # Делегируем доступ
    @property
    def profession(self):
        return self._base.comment  # Делегируем доступ
    def str(self):
        return f"{self.first_name} {self.last_name}, {self.comment}"
    def repr(self):
        return f"ShortClient({self.first_name} {self.last_name}, {self.comment})"
