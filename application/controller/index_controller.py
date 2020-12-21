from flask import render_template, request
from application import app
from application.model.entity.forum import Forum
from application.model.entity.disciplina import Disciplina
from application.model.dao.disciplina_dao import DisciplinaDAO
from application import listaForuns
from application import listaDisciplinas


@app.route('/')
def home():
    disciplina_dao = DisciplinaDAO()
    for disciplina in listaDisciplinas:
        disciplina_id = disciplina.get_id()
    disciplina = disciplina_dao.buscar_por_id(disciplina_id)
    listaDisciplinasRecentes = [listaDisciplinas[len(listaDisciplinas)-1], listaDisciplinas[len(listaDisciplinas)-2], listaDisciplinas[len(listaDisciplinas)-3]]
    listaForunsRecentes = [listaForuns[len(listaForuns)-1], listaForuns[len(listaForuns)-2], listaForuns[len(listaForuns)-3]]
    return render_template("index.html", listaDisciplinas = listaDisciplinas, listaDisciplinasRecentes = listaDisciplinasRecentes, listaForunsRecentes = listaForunsRecentes, disciplina = disciplina)
