# Salas_lab

Salas_lab é uma API para controle de agendamentos de horários para laboratórios.


## Instalação de requisitos (NECESSÁRIO:Python 3.6.0+ e pip(Atualizado))

- Crie um ambiente virtual de sua preferência (Recomendado/Opcional)

- Faça um clone do projeto: `git clone github.com/Luanlpg/Salas_lab.git`

- Acesse o repositório: `cd Salas_lab/`

- Faça a instalação do `requirements.txt` usando o comando: `pip install -r requirements.txt`

## Rodando o server da API

- Acesse o prijeto django com: `cd luizalabs`

- Rode as migrações do projeto: `python manage.py migrate`

- Crie um super user com: `python manage.py createsuperuser`

- Para rodar testes: `python manage.py test api.tests`

- Rode o servidor local com: `python manage.py runserver`

## Navegando pela API

- Faça login com o seu usuário em: `localhost:8000/admin`

- Acesse a root da API em: `localhost:8000/api/`

- Faça consultas e cadastros de salas em: `localhost:8000/api/salas/`
    - Faça edição(remover, alterar) das salas em: `localhost:8000/api/salas/<numero da sala>`

- Faça cadastros de agendamentos em: `localhost:8000/api/agendar/`
    - Só serão aceitos horários fechados:
        13:00(CORRETO)  /  13:02(INCORRETO)
        - A guarde o id de agendamento!!!

- Faça consulta de agendamentos em: `localhost:8000/api/agendamentos/`
    - Faça consulta de agendamentos com filtro de id do agendamentos em: `localhost:8000/api/agendamentos/<id de agendamento>`
    - Faça edição(remover, alterar) dos agendamentos em: `localhost:8000/api/agendamentos/<id de agendamento>`

- Faça consulta de logs em: `localhost:8000/api/logs/`
