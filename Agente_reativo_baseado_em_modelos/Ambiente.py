
from Enum_posicoes_existentes_no_ambiente_de_tarefa import Enum_posicoes_existentes_no_ambiente_de_tarefa
from Enum_estados_possiveis_do_ambiente_de_tarefa import Enum_estados_possiveis_do_ambiente_de_tarefa
import random 

class Ambiente():
    numero_de_linhas=5
    numero_de_colunas=1
    def gerar_matriz(numero_de_linhas, numero_de_colunas):
        return [random.choice(['Sujo', 'Limpo'])*numero_de_colunas for _ in range(numero_de_linhas)]
    configuraçao_do_ambiente=gerar_matriz(numero_de_linhas,numero_de_colunas)
    def o_ambiente_esta_mudando_porque_o_agente_esta_aspirando(self,posicao):
        print('Ambiente mudando')
        if posicao == Enum_posicoes_existentes_no_ambiente_de_tarefa.A.value:
            self.configuraçao_do_ambiente[0]=Enum_estados_possiveis_do_ambiente_de_tarefa.Limpo.value
        elif posicao == Enum_posicoes_existentes_no_ambiente_de_tarefa.B.value:
            self.configuraçao_do_ambiente[1]=Enum_estados_possiveis_do_ambiente_de_tarefa.Limpo.value
        elif posicao == Enum_posicoes_existentes_no_ambiente_de_tarefa.B.value:
            self.configuraçao_do_ambiente[2]=Enum_estados_possiveis_do_ambiente_de_tarefa.Limpo.value
        elif posicao == Enum_posicoes_existentes_no_ambiente_de_tarefa.B.value:
            self.configuraçao_do_ambiente[3]=Enum_estados_possiveis_do_ambiente_de_tarefa.Limpo.value
        elif posicao == Enum_posicoes_existentes_no_ambiente_de_tarefa.B.value:
            self.configuraçao_do_ambiente[4]=Enum_estados_possiveis_do_ambiente_de_tarefa.Limpo.value
    
    