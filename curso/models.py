from django.db import models

class Curso(models.Model):

  nome = models.CharField(max_length=255)
  descricao = models.TextField()
  objetivos = models.TextField()
  competencias = models.TextField()

  def __str__(self):
    return self.nome


class AreaCientifica(models.Model):

  nome = models.CharField(max_length=255)
  descricao = models.TextField()

  def __str__(self):
    return self.nome


class LinguagemProgramacao(models.Model):

  nome = models.CharField(max_length=100)

  def __str__(self):
    return self.nome


class Disciplina(models.Model):

  nome = models.CharField(max_length=255)
  ano = models.IntegerField()
  semestre = models.CharField(max_length=255)
  ects = models.IntegerField()
  curricularUnitReadableCode = models.CharField(max_length=255)
  areaCientifica = models.ForeignKey(AreaCientifica, on_delete=models.CASCADE, related_name = 'disciplinas')
  linguagensProgramacao = models.ManyToManyField(LinguagemProgramacao, null=True, blank=True, related_name = 'disciplina')
  curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name = 'curso')

  def __str__(self):
    return self.nome


class Projeto(models.Model):
  nome = models.CharField(max_length=255, blank=True, null=True)
  descricao = models.TextField()
  conceitosAplicados = models.TextField(blank=True, null=True)
  tecnologiasUsadas = models.TextField()
  imagem = models.ImageField(upload_to='curso/', blank=True, null=True)
  linkYoutube = models.URLField(blank=True, null=True)
  linkGithub = models.URLField(blank=True, null=True)
  linguagensProgramacao = models.ManyToManyField(LinguagemProgramacao, related_name = 'projetos')
  disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, null=True, blank=True, related_name = 'projeto')

  def __str__(self):
    return self.descricao



class Docente(models.Model):

  nome = models.CharField(max_length=255)

  def __str__(self):
    return self.nome

