from Enum_acoes_possiveis_de_serem_tomadas import Enum_acoes_possiveis_de_serem_tomadas
from Enum_posicoes_existentes_no_ambiente_de_tarefa import Enum_posicoes_existentes_no_ambiente_de_tarefa
from Agente import Agente
from Ambiente import Ambiente
from Respaldo_ao_programador import *
import random 
import time

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
    if acao_decidida == Enum_acoes_possiveis_de_serem_tomadas.Movimentar.value:
            escolha_de_movimentacao=random.choice(['A', 'B'])
            if escolha_de_movimentacao==agente.posicao_do_agente_naquele_momento:
                print('ATENÇÃO! A escolha aleatória de mudar de posição do agente foi igual ao local em que ele já está')
            agente.se_locomovendo(escolha_de_movimentacao)
            agente.posicao_do_agente_naquele_momento=escolha_de_movimentacao        
    if acao_decidida == Enum_acoes_possiveis_de_serem_tomadas.Nao_fazer_nada.value:
        print('**Desligando motores das rodas e do aspirador**')
        print('O aspirador está desligado na posicao {}'.format(agente.posicao_do_agente_naquele_momento))


contagem_de_percepcoes=0
while agente.percebeu_que_todos_os_espaços_estao_limpos == False or contagem_de_percepcoes>10 :
    respaldo.imprimir_o_que_esta_acontecendo(agente,ambiente,contagem_de_percepcoes)
    contagem_de_percepcoes=contagem_de_percepcoes+1
    percepcao_atual_do_agente=perceber_o_ambiente_de_tarefa(agente)
    acao_decidida_a_ser_tomada=agente.agente_reativo_baseado_em_modelo(percepcao_atual_do_agente)
    agir_no_ambiente_de_tarefa(agente,ambiente,acao_decidida_a_ser_tomada)
    print('__________________________________________________Fim do ciclo__________________________________________________\n')
    time.sleep(2)
        