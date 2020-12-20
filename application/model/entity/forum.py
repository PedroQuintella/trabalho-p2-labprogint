class Forum:

    def __init__(self, id, titulo, professor):
        self._id = id
        self._titulo = titulo
        self._professor = professor
    
    def get_id(self):
        return self._id
    
    def get_titulo(self):
        return self._titulo
    
    def get_professor(self):
        return self._professor
