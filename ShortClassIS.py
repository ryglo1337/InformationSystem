class ShortClient(Client):
    def full_info(self):
        raise NotImplementedError("Полная информация недоступна для краткой версии.")
    
    def short_info(self):
        return f"{self.last_name} {self.first_name[0]}."
