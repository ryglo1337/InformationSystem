    def full_info(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}, {self.comment}"

    def short_info(self):
        return f"{self.last_name} {self.first_name[0]}."
