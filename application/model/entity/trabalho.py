class Trabalho:

    def __init__(self, id, titulo, dataEntrega, nota):
        self._id = id
        self._titulo = titulo
        self._dataEntrega = dataEntrega
        self._nota = nota
    
    def get_id(self):
        return self._id
    
    def get_titulo(self):
        return self._titulo
    
    def get_dataEntrega(self):
        return self._dataEntrega
    
    def get_nota(self):
        return self._nota