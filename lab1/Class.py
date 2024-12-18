class Client:
    def init(self, last_name, first_name, middle_name, comment):
        # Используем сеттеры для установки значений
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.qualification = comment
       
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

  
