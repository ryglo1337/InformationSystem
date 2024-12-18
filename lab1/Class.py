class Client:
    def init(self, last_name, first_name, middle_name, comment):
        # Используем сеттеры для установки значений
        self.last_name = self.validate_last_name(last_name)
        self.first_name = self.validate_first_name(first_name)
        self.middle_name = self.validate_middle_name(middle_name)
        self.comment = self.validate_comment(qualification)
        
    # Валидация фамилии
    @staticmethod
    def validate_last_name(value):
        if not value.strip():
            raise ValueError("Last name cannot be empty.")
        if not value.isalpha():
            raise ValueError("Last name must contain only letters.")
        return value
    # Валидация имени
    @staticmethod
    def validate_first_name(value):
        if not value.strip():
            raise ValueError("First name cannot be empty.")
        if not value.isalpha():
            raise ValueError("First name must contain only letters.")
        return value
    # Валидация отчества
    @staticmethod
    def validate_middle_name(value):
        if value.strip() and not value.isalpha():
            raise ValueError("Middle name must contain only letters if provided.")
        return value
    
    # Валидация квалификации
    @staticmethod
    def validate_comment(value):
        if not value.strip():
            raise ValueError("comment cannot be empty.")
        if not value.replace(' ', '').isalpha():
            raise ValueError("comment must contain only letters and spaces.")
        return value

    
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

  
