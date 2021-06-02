
from Enum_posicoes_existentes_no_ambiente_de_tarefa import Enum_posicoes_existentes_no_ambiente_de_tarefa
from Enum_estados_possiveis_do_ambiente_de_tarefa import Enum_estados_possiveis_do_ambiente_de_tarefa


class Ambiente():
    configuraçao_do_ambiente=[Enum_estados_possiveis_do_ambiente_de_tarefa.Sujo.value,Enum_estados_possiveis_do_ambiente_de_tarefa.Sujo.value]
    def o_ambiente_esta_mudando_porque_o_agente_esta_aspirando(self,posicao):
        print('Ambiente mudando')
        if posicao == Enum_posicoes_existentes_no_ambiente_de_tarefa.A.value:
            self.configuraçao_do_ambiente[0]=Enum_estados_possiveis_do_ambiente_de_tarefa.Limpo.value
        elif posicao == Enum_posicoes_existentes_no_ambiente_de_tarefa.B.value:
            self.configuraçao_do_ambiente[1]=Enum_estados_possiveis_do_ambiente_de_tarefa.Limpo.value
            