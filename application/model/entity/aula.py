class Aula:

    def __init__(self, id, titulo):
        self._id = id
        self._titulo = titulo
    
    def get_id(self):
        return self._id
    
    def get_titulo(self):
        return self._titulo