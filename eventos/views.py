from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required # faz com que os usuarios so acessem esta url se estivem logados
def novo_evento(request):
    if request.method == "GET":
        return render(request, 'novo_evento.html')
