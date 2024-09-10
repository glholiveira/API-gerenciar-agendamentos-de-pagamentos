from django.db import models

class Agendamento(models.Model):
    data_pagamento = models.DateField()
    permite_recorrencia = models.BooleanField(default=False)
    quantidade_recorrencia = models.IntegerField(null=True, blank=True)
    intervalo_recorrencia = models.IntegerField(null=True, blank=True)
    status_recorrencia = models.CharField(max_length=20, blank=True)
    agencia = models.IntegerField()
    conta = models.IntegerField()
    valor_pagamento = models.IntegerField()

    def save(self, *args, **kwargs):
        # Converte o valor de Decimal para Inteiro antes de salvar
        self.valor_pagamento = int(self.valor_pagamento)
        super(Agendamento, self).save(*args, **kwargs)

    def __str__(self):
        return f"Agendamento {self.id} - {self.data_pagamento}"