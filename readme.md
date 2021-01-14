# Siga as Instruções Para o Teste dessa aplicação

## Dependências do Projeto:

 1. python 3.8.3
 2. Django 3.1.4
    2.1 pip install django
 3. gql 2.0.0
    3.1 pip install gql
 4. SQLite 3.0

Programas para ter acesso às informações do Banco de dados SQLite:
- HeidiSQL
- DBeaver

## Requisitos para execução 

Vá ao Arquivo, na linha 38: 
``` 
  https://github.com/danynt14/Processo-Seletivo-Prensa/blob/main/psprensa/utilities.py
````
e substitua o `${"DADO-SENSÍVEL"}` : 

```py
   # "DADO-SENSÍVEL" = client_id
   getJson = infoTableBINs(BIN, "DADO-SENSÍVEL") 
````
pelo _client_id_ da sua conta de [DEV Elo](dev.elo.com.br).

## Para subir a aplicação execute

```sh
    cd ps-prensa
    python manage-py runserver
```

entre em `%{https:localhost:8000}` e divirta-se! :-D
