from application.model.entity.disciplina import Disciplina
from application import listaDisciplinas

class DisciplinaDAO:

    def __init__(self):
        self._listaDisciplinas = listaDisciplinas
    
    def listar_disciplinas(self):
        return self._listaDisciplinas
    
    def listar_aulas(self, disciplina):
        return disciplina.get_listaAulas()

    def listar_trabalhos(self, disciplina):
        return disciplina.get_ListaTrabalhos()
    
    def listar_provas(self, disciplina):
        return disciplina.get_listaProvas()

    def buscar_por_id(self, id):
        for disciplina in range(0, len(self._listaDisciplinas)):
            if self._listaDisciplinas[disciplina].get_id() == int(id):
                return self._listaDisciplinas[disciplina]
        return None