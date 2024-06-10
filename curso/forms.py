from django import forms
from .models import Curso, Disciplina, Projeto, LinguagemProgramacao

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'descricao', 'objetivos', 'competencias']

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'ano', 'semestre', 'ects', 'curricularUnitReadableCode', 'areaCientifica', 'linguagensProgramacao', 'curso']

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'conceitosAplicados', 'tecnologiasUsadas', 'imagem', 'disciplina', 'linkYoutube', 'linkGithub', 'linguagensProgramacao']

class LinguagemProgramacaoForm(forms.ModelForm):
    class Meta:
        model = LinguagemProgramacao
        fields = ['nome']