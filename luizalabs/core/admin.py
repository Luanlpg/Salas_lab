from django.contrib import admin

from .models import Salas
from .models import Agendamentos
from .models import Logs


admin.site.register(Salas)
admin.site.register(Agendamentos)
admin.site.register(Logs)
