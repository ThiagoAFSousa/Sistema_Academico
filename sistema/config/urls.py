from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('pessoa/pessoa.html', pessoa, name='pessoas'),
    path('ocupacao/ocupacao.html', ocupacao, name='ocupacao'),
    path('cidade/cidade.html', cidade, name='cidade'),
    path('instituicao/instituicao.html', instituicao, name='instituicao'),
    path('areadosaber/areadosaber.html', areadosaber, name='areadosaber'),
    path('cursos/cursos.html', cursos, name='cursos'),

    path('semestres/semestres.html', semestres, name='semestres'),
    path('disciplinas/disciplinas.html', disciplinas, name='disciplinas'),
    path('matriculas/areas.html', matriculas, name='matriculas'),
    path('frequencia/frequencia.html', frequencia, name='frequencia'),
    path('turmas/turmas.html', turmas, name='turmas'),
    path('ocorrencias/ocorrencias.html', ocorrencias, name='ocorrencias'),
    path('disciplinasporcurso/disciplinasporcurso.html', disciplinasporcurso, name='disciplinasporcurso'),
    path('tipoavaliacao/tipoavaliacao.html', tipoavaliacao, name='tipoavaliacao'),
]

