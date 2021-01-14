from django.shortcuts import render


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect


from psprensa.utilities import toString, infoTableBINs, buscandoNumeroBIN





def index(request):
     return render(request,'viewsPrensa/index.html')

@csrf_protect
def consulta_bin(request):
    numerobin=""
    retorno = " "
    if(request.method =="POST"):
        numerobin = request.POST["codigobin"]
        if(numerobin.isnumeric()):
            if(len(numerobin) == 6):
               retorno = buscandoNumeroBIN(numerobin)
            else:
                retorno = "Erro de Validação: Digite um código que contenha apenas 6 digítos númericos!"
        else:
            retorno = "Erro de Digitação: Digite apenas números!"
    print(retorno)
       
    return render(request,'viewsPrensa/index.html',{'mensagemRetorno': retorno})

