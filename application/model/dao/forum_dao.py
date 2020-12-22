from application.model.entity.forum import Forum
from application import listaForuns

class ForumDAO:

    def __init__(self):
        self._listaForuns = listaForuns

    def buscar_por_id(self, id):
        for forum in range(0, len(self._listaForuns)):
            if self._listaForuns[forum].get_id() == int(id):
                return self._listaForuns[forum]
        return None