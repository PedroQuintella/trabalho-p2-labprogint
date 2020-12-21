from flask import render_template, request
from application import app
from application.model.entity.forum import Forum
from application.model.entity.disciplina import Disciplina
from application.model.dao.disciplina_dao import DisciplinaDAO
from application import listaForuns
from application import listaDisciplinas


@app.route("/disciplinas")
def disciplinas():
    disciplina_dao = DisciplinaDAO()
    for disciplina in listaDisciplinas:
        disciplina_id = disciplina.get_id()
    disciplina = disciplina_dao.buscar_por_id(disciplina_id)
    return render_template("disciplinas.html", listaDisciplinas = listaDisciplinas, disciplina = disciplina)