from Enum_posicoes_existentes_no_ambiente_de_tarefa import Enum_posicoes_existentes_no_ambiente_de_tarefa
import re
import time 
import random

class Agente():
    percepcao_atual=[]
    objetivo_principal=False
    todos_os_locais_que_o_aspirador_passou=[]
    percebeu_que_todos_os_espaços_estao_limpos=False
    contagem_de_vezes_que_o_agente_passou_por_A=0
    contagem_de_vezes_que_o_agente_passou_por_B=0
    contagem_de_vezes_que_o_agente_passou_por_C=0
    contagem_de_vezes_que_o_agente_passou_por_D=0
    contagem_de_vezes_que_o_agente_passou_por_E=0
    posicao_do_agente_naquele_momento=Enum_posicoes_existentes_no_ambiente_de_tarefa.A.value
    def agente_baseado_em_objetivos(self,percepcao):
        self.percepcao_atual.append(self.posicao_do_agente_naquele_momento+', '+percepcao)
        print('O agente está consultando os objetivos para formular qual a melhor instrução a tomar nesse momento.')
        decisao_a_ser_executada=self.refletir_o_que_deve_ser_feito_acessando_o_guia_com_as_instrucoes(self.percepcao_atual)
        print('A decisao tomada foi: {}'.format(decisao_a_ser_executada))
        return decisao_a_ser_executada


    def se_locomovendo(self,local_pretendido):
        print('**ligando o motor das rodas do aspirador**')
        print('** FZENDO BARULHO ** VRUUUMMMM ')
        print('O aspirador se locomoveu para a posicao {}'.format(local_pretendido))
        self.posicao_do_agente_naquele_momento=local_pretendido
        self.todos_os_locais_que_o_aspirador_passou.append(local_pretendido)
        
    def aspirando_sujeira(self,posicao_do_agente):
        print('**ligando o motor do aspirador**')
        print('** FZENDO BARULHO ** BZZZZZZZZZZZZZZZZZZZZZ ')
        print('O aspirador está retirando sujeira na posicao {}'.format(self.posicao_do_agente_naquele_momento))
        if self.posicao_do_agente_naquele_momento==Enum_posicoes_existentes_no_ambiente_de_tarefa.A.value:
            self.contagem_de_vezes_que_o_agente_passou_por_A=self.contagem_de_vezes_que_o_agente_passou_por_A+1
        if self.posicao_do_agente_naquele_momento==Enum_posicoes_existentes_no_ambiente_de_tarefa.B.value:
            self.contagem_de_vezes_que_o_agente_passou_por_A=self.contagem_de_vezes_que_o_agente_passou_por_B+1
        if self.posicao_do_agente_naquele_momento==Enum_posicoes_existentes_no_ambiente_de_tarefa.C.value:
            self.contagem_de_vezes_que_o_agente_passou_por_A=self.contagem_de_vezes_que_o_agente_passou_por_C+1
        if self.posicao_do_agente_naquele_momento==Enum_posicoes_existentes_no_ambiente_de_tarefa.D.value:
            self.contagem_de_vezes_que_o_agente_passou_por_A=self.contagem_de_vezes_que_o_agente_passou_por_D+1
        if self.posicao_do_agente_naquele_momento==Enum_posicoes_existentes_no_ambiente_de_tarefa.E.value:
            self.contagem_de_vezes_que_o_agente_passou_por_A=self.contagem_de_vezes_que_o_agente_passou_por_E+1

    def refletir_o_que_deve_ser_feito_acessando_o_guia_com_as_instrucoes(self,percepcao_atual):
        print('A percepcao completa atualizada é {}'.format(str(self.percepcao_atual)))
        print('A percepcao atual é {}'.format(str(self.percepcao_atual[-1])))
        contagens_de_locais_limpos=0
        if 'A' in self.todos_os_locais_que_o_aspirador_passou :
            contagens_de_locais_limpos=contagens_de_locais_limpos+1
        if 'B' in self.todos_os_locais_que_o_aspirador_passou :
            contagens_de_locais_limpos=contagens_de_locais_limpos+1
        if 'C' in self.todos_os_locais_que_o_aspirador_passou :
            contagens_de_locais_limpos=contagens_de_locais_limpos+1
        if 'D' in self.todos_os_locais_que_o_aspirador_passou :
            contagens_de_locais_limpos=contagens_de_locais_limpos+1
        if 'E' in self.todos_os_locais_que_o_aspirador_passou :
            contagens_de_locais_limpos=contagens_de_locais_limpos+1
        print('Contagem de locais limpos: {}'.format(contagens_de_locais_limpos))
        if contagens_de_locais_limpos>4:
            self.percebeu_que_todos_os_espaços_estao_limpos=True
        if 'Sujo' in self.percepcao_atual[-1]:
            print('A percepção tem o ambiente sujo')
            return 'Aspirar'
        else:
            return 'Movimentar'

    def quais_as_escolhas_de_movimentacao(self,posicao_do_agente_naquele_momento):
        if posicao_do_agente_naquele_momento == Enum_posicoes_existentes_no_ambiente_de_tarefa.A.value:
            return Enum_posicoes_existentes_no_ambiente_de_tarefa.B.value
        if posicao_do_agente_naquele_momento == Enum_posicoes_existentes_no_ambiente_de_tarefa.B.value:
            return random.choice([Enum_posicoes_existentes_no_ambiente_de_tarefa.A.value, Enum_posicoes_existentes_no_ambiente_de_tarefa.C.value])
        if posicao_do_agente_naquele_momento == Enum_posicoes_existentes_no_ambiente_de_tarefa.C.value:
            return random.choice([Enum_posicoes_existentes_no_ambiente_de_tarefa.B.value, Enum_posicoes_existentes_no_ambiente_de_tarefa.D.value])
        if posicao_do_agente_naquele_momento == Enum_posicoes_existentes_no_ambiente_de_tarefa.D.value:
            return random.choice([Enum_posicoes_existentes_no_ambiente_de_tarefa.C.value, Enum_posicoes_existentes_no_ambiente_de_tarefa.E.value])
        if posicao_do_agente_naquele_momento == Enum_posicoes_existentes_no_ambiente_de_tarefa.E.value:
            return Enum_posicoes_existentes_no_ambiente_de_tarefa.D.value
        return Enum_posicoes_existentes_no_ambiente_de_tarefa.A.value