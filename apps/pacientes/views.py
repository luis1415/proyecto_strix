from django.shortcuts import render, redirect
from apps.pacientes.forms import PacienteForm
# Create your views here.


def index(request):
    return render(request, 'paciente/index.html')


def paciente_view(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('paciente:index')
    else:
        form = PacienteForm()

    return render(request, 'paciente/paciente_form.html', {'form': form})
