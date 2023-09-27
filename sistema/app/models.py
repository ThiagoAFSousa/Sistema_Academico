from django.db import models

class Ocupacao(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Instituicao(models.Model):
     nome = models.CharField(max_length=50)
     site = models.CharField(max_length=50)
     telefone = models.CharField(max_length=50)
     def __str__(self):
        return self.nome

class AreasdoSaber(models.Model):
     nome = models.CharField(max_length=50)
     def __str__(self):
        return self.nome

class Cursos(models.Model):
     nome = models.CharField(max_length=50)
     carga_horaria_total = models.CharField(max_length=50)
     duracao_meses = models.CharField(max_length=50)
     areasaber = models.ForeignKey(AreasdoSaber,on_delete=models.CASCADE)
     instituicao = models.ForeignKey(Instituicao,on_delete=models.CASCADE)
     def __str__(self):
        return self.nome

class Semestre(models.Model):
     nome = models.CharField(max_length=50)
     def __str__(self):
        return self.nome

class Disciplinas(models.Model):
     nome = models.CharField(max_length=50)
     areasaber = models.ForeignKey(AreasdoSaber,on_delete=models.CASCADE)
     def __str__(self):
        return self.nome

class Frequencia(models.Model):
     curso = models.ForeignKey(Cursos,on_delete=models.CASCADE)
     disciplina = models.ForeignKey(Disciplinas,on_delete=models.CASCADE)
     numero_faltas = models.CharField(max_length=50)
     def __str__(self):
        return self.numero_faltas

class Turmas(models.Model):
     nome = models.CharField(max_length=50)
     periodo_semestre = models.CharField(max_length=50)
     def __str__(self):
        return self.nome

class Cidade(models.Model):
     nome = models.CharField(max_length=50)
     uf = models.CharField(max_length=2)
     def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    pai = models.CharField(max_length=50)
    mae = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    data_nasc = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE)
    ocupacao = models.ForeignKey(Ocupacao,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    

class Matriculas(models.Model):
     instituicao = models.ForeignKey(Instituicao,on_delete=models.CASCADE)
     curso = models.ForeignKey(Cursos,on_delete=models.CASCADE)
     pessoa = models.ForeignKey(Pessoa,on_delete=models.CASCADE)
     data_inicio = models.CharField(max_length=50)
     data_previsao_termino = models.CharField(max_length=50)
     def __str__(self):
        return self.data_inicio

class Ocorrencias(models.Model):
     descricao = models.CharField(max_length=50)
     data = models.CharField(max_length=50)
     curso = models.ForeignKey(Cursos,on_delete=models.CASCADE)
     disciplina = models.ForeignKey(Disciplinas,on_delete=models.CASCADE)
     pessoa = models.ForeignKey(Pessoa,on_delete=models.CASCADE)
     def __str__(self):
        return self.descricao

class DisciplinasCursos(models.Model):
     nome = models.CharField(max_length=50)
     carga_horaria = models.CharField(max_length=50)
     curso = models.ForeignKey(Cursos,on_delete=models.CASCADE)
     periodo = models.ForeignKey(Semestre,on_delete=models.CASCADE)
     def __str__(self):
        return self.nome

class TipoAvaliacao(models.Model):
     nome = models.CharField(max_length=50)
     def __str__(self):
        return self.nome

class Avaliacao(models.Model):
     descricao = models.CharField(max_length=50)
     curso = models.ForeignKey(Cursos,on_delete=models.CASCADE)
     disciplina = models.ForeignKey(Disciplinas,on_delete=models.CASCADE)
     tipoavaliacao = models.ForeignKey(TipoAvaliacao,on_delete=models.CASCADE)
     def __str__(self):
        return self.descricao
     

