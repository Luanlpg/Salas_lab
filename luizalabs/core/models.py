from django.db import models


STATUS_CHOICES = (
    ('disponivel', 'DISPONIVEL'),
    ('indisponivel', 'INDISPONIVEL')
)
SERVICE_CHOICES = (
    ('agendamento', 'AGENDAMENTO'),
    ('cancelamento', 'CANCELAMENTO'),
    ('cadastro', 'CADASTRO')
)


class Salas(models.Model):
    numero = models.IntegerField(primary_key=True, unique=True)
    capacidade = models.IntegerField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    obs = models.CharField(max_length=200)


class Agendamentos(models.Model):
    titulo = models.CharField(max_length=200)
    sala = models.ForeignKey(Salas, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    inicio = models.DateTimeField()
    termino = models.DateTimeField()


class Logs(models.Model):
    sala = models.ForeignKey(Salas, on_delete=models.CASCADE)
    log = models.CharField(max_length=200)
    service = models.CharField(max_length=25)
    data = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Validação do campo service.
        """
        options_service = ['AGENDAMENTO',
                            'CANCELAMENTO',
                            'CADASTRO',
                            'EDIÇÃO',
                            'REMOÇÃO'
                            ]

        if self.service not in options_service:
            raise Exception('Invalid service!')
        super(Logs, self).save(*args, **kwargs)


"""Esse sistema deve receber requisições de agendamento contendo título, sala e período de agendamento e
deve apenas reservar a sala, se a sala requisitada estiver disponível. Caso contrário, deve apresentar um
erro."""
