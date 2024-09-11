## Gerenciamento de Agendamentos / Pagamentos 

Este projeto é uma API RESTful construída com Django e Django REST Framework para gerenciar agendamentos de pagamentos. A API suporta operações como listar, criar, consultar e deletar agendamentos utilizando métodos HTTP (GET, POST, DELETE) com uma única URL para cada operação.

# Requisitos

    Python 3.x
    Django 5.1.1
    Django REST Framework


## Instalação
#### Clone este repositório:
```bash
git clone https://github.com/glholiveira/API-gerenciar-agendamentos-de-pagamentos.git
 ```
#### Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate  

No Windows, use 'venv\Scripts\activate'
```
#### Instale as dependências:
```bash    
pip install -r requirements.txt
   ```
#### Acesse a pasta do projeto 
```bash    
cd pagamento_project/
   ```
#### Execute as migrações do banco de dados:
```python
python manage.py migrate
   ```
## Inicie o servidor de desenvolvimento:
```python
python manage.py runserver
 ```
# Uso da API:

#### Endpoints
    
    Listar agendamentos
        GET /api/agendamentos/
        Retorna todos os agendamentos cadastrados.
    
    Consultar agendamento por ID
        GET /api/agendamentos/{id}/
        Retorna o agendamento específico pelo ID.
    
    Criar agendamento
        POST /api/agendamentos/
        Cria um novo agendamento. Enviar um JSON com os dados do agendamento no corpo da requisição.
    json
    
    {
      "data_pagamento": "2024-11-10",
      "permite_recorrencia": true,
      "quantidade_recorrencia": 1,
      "intervalo_recorrencia": 30,
      "status_recorrencia": "ativo",
      "agencia": 124545434545,
      "conta": 56555789,
      "valor_pagamento": 25.50
    }
    
    
    Deletar agendamento
        DELETE /api/agendamentos/{id}/
        Deleta um agendamento específico pelo ID.
    
# Testes
Para rodar os testes, use o comando:

python manage.py test
