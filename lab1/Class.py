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

  
