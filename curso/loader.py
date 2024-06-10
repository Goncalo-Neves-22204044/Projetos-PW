from curso.models import Curso, AreaCientifica, Disciplina, Projeto, LinguagemProgramacao, Docente
import json

Curso.objects.all().delete()
Disciplina.objects.all().delete()
AreaCientifica.objects.all().delete()
Projeto.objects.all().delete()
LinguagemProgramacao.objects.all().delete()
Docente.objects.all().delete()

with open('curso/json/LEI.json') as f:

    dados = json.load(f)
    detalhesCurso = dados["courseDetail"]

    areaCientifica = AreaCientifica.objects.create(
        nome = detalhesCurso["scientificArea"]
    )

    curso = Curso.objects.create(
        nome = detalhesCurso["courseName"],
        objetivos = detalhesCurso["objectives"],
        descricao = detalhesCurso["presentation"],
        competencias = detalhesCurso["competences"]
    )

    disciplinas = dados["courseFlatPlan"]

    for disciplina in disciplinas:
        Disciplina.objects.create(
            nome = disciplina["curricularUnitName"],
            ano = disciplina["curricularYear"],
            semestre = disciplina["semester"],
            ects = disciplina["ects"],
            curricularUnitReadableCode = disciplina["curricularIUnitReadableCode"],
            areaCientifica = areaCientifica,
            curso = curso
        )

    linguagens = ["Python", "Java", "JavaScipt", "HTML", "CSS", "Kotlin", "C", "C++", "C#", "Ruby", "Go", "Assembly", "Cobol"]

    for linguagem in linguagens:
        LinguagemProgramacao.objects.create(
            nome = linguagem
        )