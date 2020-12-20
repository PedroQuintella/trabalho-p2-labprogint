from flask import Flask
import os
from application.model.entity.forum import Forum
from application.model.entity.aula import Aula
from application.model.entity.trabalho import Trabalho
from application.model.entity.prova import Prova
from application.model.entity.disciplina import Disciplina

app = Flask (__name__, static_folder=os.path.abspath("application/view/static"), template_folder=os.path.abspath("application/view/templates"))


forum1 = Forum(1, "Fórum de Modelagem de Banco de Dados", "Anrafel Fernandes")
forum2 = Forum(2, "Fórum de Sistemas Operacionais", "Luis Felipe Melo")
forum3 = Forum(3, "Fórum de Gestão Ambiental", "Cleber Paschoal")
forum4 = Forum(4, "Fórum de Gestão Estratégica de Pessoas", "Claudenir do Val")
forum5 = Forum(5, "Fórum de Legislação Aplicada à Informática", "Maria Fernanda Ricci")
forum6 = Forum(6, "Fórum de Empreendedorismo e Inovação", "Marco Antônio Araújo")

listaForuns = [forum1, forum2, forum3, forum4, forum5, forum6]



disciplina1 = Disciplina(1, "Modelagem de Banco de Dados", "Anrafel Fernandes", forum1, [Aula(1, "Aula 1: Introdução a SGBDs")], [Trabalho(1, "Trabalho P1", "20/09/2020", 2), Trabalho(2, "Trabalho P2", "22/11/2020", 1.5)], [Prova(1, "Prova P1", "20/09/2020", 7), Prova(2, "Prova P2", "22/11/2020", 6.5)])

disciplina2 = Disciplina(2, "Sistemas Operacionais", "Luis Felipe Melo", forum2, [Aula(1, "Aula 1: Introdução a Sistemas Operacionais")], [Trabalho(1, "Trabalho P1", "21/09/2020", 2), Trabalho(2, "Trabalho P2", "23/11/2020", 2)], [Prova(1, "Prova P1", "21/09/2020", 8), Prova(2, "Prova P2", "23/11/2020", 7)])

disciplina3 = Disciplina(3, "Gestão Ambiental", "Cleber Paschoal", forum3, [Aula(1, "Aula 1: O que é Gestão Ambiental")], [Trabalho(1, "Trabalho P1", "22/09/2020", 2), Trabalho(2, "Trabalho P2", "24/11/2020", 2)], [Prova(1, "Prova P1", "22/09/2020", 8), Prova(2, "Prova P2", "24/11/2020", 8)])

disciplina4 = Disciplina(4, "Gestão Estratégica de Pessoas", "Claudenir do Val", forum4, [Aula(1, "Aula 1: Gestão de Pessoas")], [Trabalho(1, "Trabalho P1", "24/09/2020", 2), Trabalho(2, "Trabalho P2", "25/11/2020", 1)], [Prova(1, "Prova P1", "24/09/2020", 8), Prova(2, "Prova P2", "25/11/2020", 6)])

disciplina5 = Disciplina(5, "Legislação Aplicada à Informática", "Maria Fernanda Ricci", forum5, [Aula(1, "Aula 1: Introdução à Legislação")], [Trabalho(1, "Trabalho P1", "25/09/2020", 2), Trabalho(2, "Trabalho P2", "26/11/2020", 2)], [Prova(1, "Prova P1", "25/09/2020", 8), Prova(2, "Prova P2", "26/11/2020", 7.5)])

disciplina6 = Disciplina(6, "Empreendedorismo e Inovação", "Marco Antônio Araújo", forum6, [Aula(1, "Aula 1: Projeto de Empreendedorismo")], [Trabalho(1, "Trabalho P1", "26/09/2020", 2), Trabalho(2, "Trabalho P2", "27/11/2020", 2)], [Prova(1, "Prova P1", "26/09/2020", 8), Prova(2, "Prova P2", "27/11/2020", 8)])

listaDisciplinas = [disciplina1, disciplina2, disciplina3, disciplina4, disciplina5, disciplina6]