from rest_framework import serializers
from .models import Agendamento

class AgendamentoSerializerGravacao(serializers.ModelSerializer):
    valor_pagamento = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)

    class Meta:
        model = Agendamento
        fields = '__all__'

    def validate_valor_pagamento(self, value):
        # Converte o valor decimal para inteiro antes de salvar
        return int(value * 100)  # Multiplica por 100 para preservar até 2 casas decimais


class AgendamentoSerializerLeitura(serializers.ModelSerializer):
    valor_pagamento = serializers.IntegerField()

    class Meta:
        model = Agendamento
        fields = '__all__'

    