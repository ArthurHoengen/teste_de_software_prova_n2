class Task:
    def __init__(self, id : int, description : str, done : bool):
        self.__id = id
        self.__description = description
        self.__done = done
    
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_description(self):
        return self.__description
    
    def set_description(self, description):
        self.__description = description
    
    def get_done(self):
        return self.__done
    
    def set_done(self, done):
        self.__done = done