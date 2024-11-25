def __init__(self, last_name: str, first_name: str, middle_name: Optional[str] = None, comment: str = ""):
        self.__last_name = self.validate_name(last_name)
        self.__first_name = self.validate_name(first_name)
        self.__middle_name = middle_name
        self.__comment = self.validate_comment(comment)

    @classmethod
    def from_json(cls, json_data: str):
        data = json.loads(json_data)
        return cls(
            last_name=data["last_name"],
            first_name=data["first_name"],
            middle_name=data.get("middle_name"),
            comment=data.get("comment", "")
        )
