class Taks:
    def __init__(self,id, title, description, completed=False):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__completed = completed

    def get_id(self):
        return self.__id

    def set_id(self, value):
        self.__id = value

    def get_title(self):
        return self.__title

    def set_title(self, value):
        self.__title = value

    def get_description(self):
        return self.__description

    def set_description(self, value):
        self.__description = value

    def get_completed(self):
        return self.__completed

    def set_completed(self, value):
        self.__completed = value

    def to_dict(self):
        return {"id": self.get_id(), "title": self.get_title(),"description": self.get_description(),"completed": self.get_completed()}