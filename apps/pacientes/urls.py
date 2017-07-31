from django.conf.urls import url

from apps.pacientes.views import index, paciente_view

urlpatterns = [
    url(r'^index$', index, name='index'),
    url(r'^nuevo', paciente_view, name='paciente_crear'),
]
