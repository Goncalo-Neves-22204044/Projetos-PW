from django.shortcuts import render, redirect
from .models import Curso, Disciplina, Projeto, LinguagemProgramacao
from .forms import CursoForm, DisciplinaForm, ProjetoForm, LinguagemProgramacaoForm
from django.contrib.auth.decorators import login_required

def user_belongs_to_group(user, group):
    return user.groups.filter(name=group).exists()

def cursos_view(request):
    cursos = Curso.objects.all()
    canUserManipulate = request.user.groups.filter(name='Editores de cursos').exists()

    context = {'cursos': cursos,'canUserManipulate':canUserManipulate}

    return render(request, 'curso/curso.html', context)

def curso_details_view(request, curso_id):
    disciplinas = Disciplina.objects.filter(curso=curso_id)
    canUserManipulate = request.user.groups.filter(name='Editores de cursos').exists()

    context = {'curso': Curso.objects.get(pk=curso_id), 'disciplinas': disciplinas, 'canUserManipulate':canUserManipulate}

    return render(request, 'curso/curso_details.html', context)

def disciplina(request, disciplina_id):
    disciplina = Disciplina.objects.get(pk=disciplina_id)
    projetos = Projeto.objects.filter(disciplina=disciplina_id)
    linguagens = LinguagemProgramacao.objects.filter(disciplina=disciplina_id)
    canUserManipulate = request.user.groups.filter(name='Editores de cursos').exists()

    context = {'disciplina': disciplina, 'projetos': projetos, 'linguagens': linguagens, 'canUserManipulate':canUserManipulate}

    return render(request, 'curso/disciplina.html', context)


def projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(pk=projeto_id)
    canUserManipulate = request.user.groups.filter(name='Editores de cursos').exists()

    context = {'projeto': projeto, 'canUserManipulate':canUserManipulate}

    return render(request, 'curso/projeto.html', context)

def linguagem_view(request, linguagem_id):
    linguagem = LinguagemProgramacao.objects.get(pk=linguagem_id)
    disciplinas = Disciplina.objects.filter(linguagensProgramacao=linguagem_id)
    canUserManipulate = request.user.groups.filter(name='Editores de cursos').exists()

    context = {'linguagem': linguagem, 'disciplinas': disciplinas, 'canUserManipulate':canUserManipulate}

    return render(request, 'curso/linguagem.html', context)

################################################################################
#
#                                   Curso
#
################################################################################

@login_required
def create_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.save()
            return redirect('curso:curso_details', curso.id)
    else:
        form = CursoForm()
    return render(request, 'curso/create_curso.html', {'form': form})

@login_required
def edit_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance = curso)
        if form.is_valid():
            form.save()
            return redirect('curso:curso_details', curso.id)
    else:
        form = CursoForm(instance=curso)
    return render(request, 'curso/edit_curso.html', {'form': form, 'curso': curso})

@login_required
def delete_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    if request.method == 'POST':
        curso.delete()
        return redirect('curso:cursos')

    return render(request, 'curso/delete_curso.html', {'curso': curso})


################################################################################
#
#                                   Disciplina
#
################################################################################

@login_required
def create_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            disciplina = form.save(commit=False)
            disciplina.save()
            return redirect('curso:disciplina', disciplina.id)
    else:
        form = DisciplinaForm()
    return render(request, 'curso/create_disciplina.html', {'form': form})

@login_required
def edit_disciplina(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance = disciplina)
        if form.is_valid():
            form.save()
            return redirect('curso:disciplina', disciplina_id)
    else:
        form = DisciplinaForm(instance=disciplina)
    return render(request, 'curso/edit_disciplina.html', {'form': form, 'disciplina': disciplina})

@login_required
def delete_disciplina(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    if request.method == 'POST':
        disciplina.delete()
        return redirect('curso:curso_details', disciplina.curso.id)
    return render(request, 'curso/delete_disciplina.html', {'disciplina': disciplina})


################################################################################
#
#                                   Projeto
#
################################################################################

@login_required
def create_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.save()
            return redirect('curso:disciplina', projeto.disciplina.id)

    else:
        form = ProjetoForm()
    return render(request, 'curso/create_projeto.html', {'form': form})

@login_required
def edit_projeto(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('curso:projeto', projeto_id)
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'curso/edit_projeto.html', {'form': form, 'projeto': projeto})

@login_required
def delete_projeto(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('curso:disciplina', projeto.disciplina.id)
    return render(request, 'curso/delete_projeto.html', {'projeto': projeto})

################################################################################
#
#                                   LinguagemProgramacao
#
################################################################################

@login_required
def create_linguagem(request):
    if request.method == 'POST':
        form = LinguagemProgramacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso:cursos')
    else:
        form = LinguagemProgramacaoForm()
    return render(request, 'curso/create_linguagem.html', {'form': form})

@login_required
def edit_linguagem(request, linguagem_id):
    linguagem = LinguagemProgramacao.objects.get(id=linguagem_id)
    if request.method == 'POST':
        form = LinguagemProgramacaoForm(request.POST, instance=linguagem)
        if form.is_valid():
            form.save()
            return redirect('curso:linguagem', linguagem.id )
    else:
        form = LinguagemProgramacaoForm(instance=linguagem)
    return render(request, 'curso/edit_linguagem.html', {'form': form, 'linguagem': linguagem})

@login_required
def delete_linguagem(request, linguagem_id):
    linguagem = LinguagemProgramacao.objects.get(id=linguagem_id)
    if request.method == 'POST':
        linguagem.delete()
        return redirect('curso:cursos')
    return render(request, 'curso/delete_linguagem.html', {'linguagem': linguagem})







