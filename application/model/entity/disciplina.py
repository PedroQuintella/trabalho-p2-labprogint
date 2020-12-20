class Disciplina:

    def __init__(self, id, nome, professor, forum, listaAulas, listaTrabalhos, listaProvas):
        self._id = id
        self._nome = nome
        self._professor = professor
        self._forum = forum
        self._listaAulas = listaAulas
        self._listaTrabalhos = listaTrabalhos
        self._listaProvas = listaProvas

    def get_id(self):
        return self._id
    
    def get_nome(self):
        return self._nome

    def get_professor(self):
        return self._professor

    def get_forum(self):
        return self._forum
    
    def get_listaAulas(self):
        return self._listaAulas

    def get_ListaTrabalhos(self):
        return self._listaTrabalhos
    
    def get_listaProvas(self):
        return self._listaProvas