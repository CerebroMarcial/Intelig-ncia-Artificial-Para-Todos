from Enum_acoes_possiveis_de_serem_tomadas import Enum_acoes_possiveis_de_serem_tomadas
from Enum_posicoes_existentes_no_ambiente_de_tarefa import Enum_posicoes_existentes_no_ambiente_de_tarefa
from Agente import Agente
from Ambiente import Ambiente
from Respaldo_ao_programador import *

agente=Agente()
ambiente=Ambiente()
respaldo=Respaldo_ao_programador()

def perceber_o_ambiente_de_tarefa(agente):
    percepcao_do_agente=''
    if agente.posicao_do_agente_naquele_momento == Enum_posicoes_existentes_no_ambiente_de_tarefa.A.value:
        percepcao_do_agente=ambiente.configuraçao_do_ambiente[0]
    elif agente.posicao_do_agente_naquele_momento == Enum_posicoes_existentes_no_ambiente_de_tarefa.B.value:
        percepcao_do_agente=ambiente.configuraçao_do_ambiente[1]
    return percepcao_do_agente

def agir_no_ambiente_de_tarefa(agente,ambiente,acao_decidida):
    if acao_decidida == Enum_acoes_possiveis_de_serem_tomadas.Aspirar.value:
        ambiente.o_ambiente_esta_mudando_porque_o_agente_esta_aspirando(agente.posicao_do_agente_naquele_momento)
        agente.aspirando_sujeira(agente.posicao_do_agente_naquele_momento)
    if acao_decidida == Enum_acoes_possiveis_de_serem_tomadas.Esquerda.value:
        agente.se_locomovendo_para_a_esquerda(Enum_posicoes_existentes_no_ambiente_de_tarefa.A.value)
        agente.posicao_do_agente_naquele_momento=Enum_posicoes_existentes_no_ambiente_de_tarefa.A.value
    if acao_decidida == Enum_acoes_possiveis_de_serem_tomadas.Direita.value:
        agente.se_locomovendo_para_a_esquerda(Enum_posicoes_existentes_no_ambiente_de_tarefa.B.value)
        agente.posicao_do_agente_naquele_momento=Enum_posicoes_existentes_no_ambiente_de_tarefa.B.value
    if acao_decidida == Enum_acoes_possiveis_de_serem_tomadas.Nao_fazer_nada.value:
        print('**Desligando motores das rodas e do aspirador**')
        print('O aspirador está desligado na posicao {}'.format(agente.posicao_do_agente_naquele_momento))


contagem_de_percepcoes=10
for contagem in range(contagem_de_percepcoes):
    respaldo.imprimir_o_que_esta_acontecendo(agente,ambiente)
    percepcao_atual_do_agente=perceber_o_ambiente_de_tarefa(agente)
    acao_decidida_a_ser_tomada=agente.agente_dirigido_por_tabela(percepcao_atual_do_agente)
    agir_no_ambiente_de_tarefa(agente,ambiente,acao_decidida_a_ser_tomada)
    print('Fim do ciclo __________________________________________________\n')
        