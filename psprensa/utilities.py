from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

from psprensa.models import TabelaBin

def toString(numero,issuer_name,product_name,brand_name, country,is_international,is_company,is_token):
    return 'BIN: %s \nEmissor do Cartão: %s \nNome do Produto: %s \nBandeira: %s \nPaís: %s \nInternacional: %s \nCartão Coorporativo: %s \nCartão Virtual %s' %(numero,issuer_name,product_name,brand_name, country,is_international,is_company,is_token)

def infoTableBINs(BIN,dado_sensivel_client_ID):
    informacoesHTTP=RequestsHTTPTransport(
        url='https://hml-api.elo.com.br/graphql',
        use_json=True,
        headers={
            "Content-type": "application/json",
            "client_id": dado_sensivel_client_ID 
        },
    )
   
    cliente = Client(transport=informacoesHTTP, fetch_schema_from_transport=True)
    query = "query OneBin {  bin(number: \" "+  str(BIN) +" \") { issuer { name } product { name } brand{ name } country isInternational  isCompany isToken }}"
    consulta = gql(query)
    return cliente.execute(consulta)

def buscandoNumeroBIN(BIN):
    existeBINBanco = TabelaBin.objects.filter(numero=BIN).count()
    if(existeBINBanco > 0):
        existeBINBanco = TabelaBin.objects.filter(numero=BIN)
        return toString(BIN, 
                 existeBINBanco[0].issuer_name, 
                 existeBINBanco[0].product_name, 
                 existeBINBanco[0].brand_name,
                 existeBINBanco[0].country, 
                 existeBINBanco[0].is_international, 
                 existeBINBanco[0].is_company, 
                 existeBINBanco[0].is_token)
    else:
        try:
            getJson = infoTableBINs(BIN, "DADO-SENSÍVEL")
             
        except:
            return "Numero Bin Inválido"
        try:
            adicionarTabelaBin = TabelaBin(
                                    numero = BIN,
                                    issuer_name = getJson['bin']['issuer']['name'],
                                    product_name = getJson['bin']['product']['name'],
                                    brand_name =  getJson['bin']['brand']['name'],
                                    country = getJson['bin']['country'],
                                    is_international = getJson['bin']['isInternational'],
                                    is_company = getJson['bin']['isCompany'],
                                    is_token = getJson['bin']['isToken'])
            adicionarTabelaBin.save()
            return toString(BIN, getJson['bin']['issuer']['name'], 
                            getJson['bin']['product']['name'], 
                            getJson['bin']['brand']['name'],
                            getJson['bin']['country'], 
                            getJson['bin']['isInternational'], 
                            getJson['bin']['isCompany'], 
                            getJson['bin']['isToken'])
        except:
            return "Erro 404: Erro Interno"
