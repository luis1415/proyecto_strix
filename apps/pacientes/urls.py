from django.conf.urls import url

from apps.pacientes.views import index

urlpatterns = [
    url(r'^index$', index),
]