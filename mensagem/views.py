from django.shortcuts import render, redirect
from .models import Mensagem

def jardim_view(request):
    if request.method == "POST":
        texto = request.POST.get("mensagem")
        if texto:
            Mensagem.objects.create(texto=texto)
            return redirect("jardim")
    mensagens = Mensagem.objects.order_by('-criada_em')
    return render(request, "jardim.html", {"mensagem": mensagens})