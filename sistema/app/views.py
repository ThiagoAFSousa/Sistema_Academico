from django.shortcuts import render
from . models  import *

def pessoa(request):
    pessoas = {
         'pessoa':Pessoa.objects.all()
        }

    return render(request,'pessoa/pessoa.html',pessoas)

def ocupacao(request):
    ocupacao = {
         'ocupacao':Ocupacao.objects.all()
        }

    return render(request,'ocupacao/ocupacao.html', ocupacao)

def cidade(request):
    cidade = {
         'cidade':Cidade.objects.all()
        }

    return render(request,'cidade/cidade.html', cidade)

def instituicao(request):
    instituicao = {
         'instituicao':Instituicao.objects.all()
        }

    return render(request,'instituicao/instituicao.html', instituicao)

def areadosaber(request):
    areadosaber = {
         'areadosaber':AreasdoSaber.objects.all()
        }

    return render(request,'areadosaber/areadosaber.html', areadosaber)

def cursos(request):
    cursos = {
         'cursos':Cursos.objects.all()
        }

    return render(request,'cursos/cursos.html', cursos)

def semestres(request):
    semestres = {
         'semestres':Semestre.objects.all()
        }

    return render(request,'semestre/semestre.html', semestres)

def disciplinas(request):
    disciplinas = {
         'disciplinas':Disciplinas.objects.all()
        }

    return render(request,'disciplinas/disciplinas.html', disciplinas)

def matriculas(request):
    matriculas = {
         'matriculas':Matriculas.objects.all()
        }

    return render(request,'matriculas/matriculas.html', matriculas)

def frequencia(request):
    frequencia = {
         'frequencia':Frequencia.objects.all()
        }

    return render(request,'frequencia/frequencia.html', frequencia)

def turmas(request):
    turmas = {
         'turmas':Turmas.objects.all()
        }

    return render(request,'turmas/turmas.html', turmas)

def ocorrencias(request):
    ocorrencias = {
         'ocorrencias':Ocorrencias.objects.all()
        }

    return render(request,'ocorrencias/ocorrencias.html', ocorrencias)

def disciplinasporcurso(request):
    disciplinasporcurso = {
         'disciplinasporcurso':DisciplinasCursos.objects.all()
        }

    return render(request,'disciplinasporcurso/disciplinasporcurso.html', disciplinasporcurso)

def tipoavaliacao(request):
    tipoavaliacao = {
         'tipoavaliacao':TipoAvaliacao.objects.all()
        }

    return render(request,'tipoavaliacao/tipoavaliacao.html', tipoavaliacao)

def avaliacao(request):
    avaliacao = {
         'avaliacao':Avaliacao.objects.all()
        }

    return render(request,'avaliacao/avaliacao.html', avaliacao)










