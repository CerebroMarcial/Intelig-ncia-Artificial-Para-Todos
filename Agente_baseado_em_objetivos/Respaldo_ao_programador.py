
class Respaldo_ao_programador():
    def imprimir_o_que_esta_acontecendo(self,agente,ambiente,contagem_de_percepcoes):
        print('Início do novo ciclo!\nEssa é a {}° percepcao do agente'.format(contagem_de_percepcoes))
        print('O agente está na posicao {}'.format(agente.posicao_do_agente_naquele_momento))
        print('A configuracao do tabuleiro está assim : {}'.format(ambiente.configuraçao_do_ambiente))
        print('O agente já observou os seguintes locais : {}'.format(agente.todos_os_locais_que_o_aspirador_passou))
        print('O agente passou pela posição A {} vezes.'.format(agente.contagem_de_vezes_que_o_agente_passou_por_A))
        print('O agente passou pela posição B {} vezes.'.format(agente.contagem_de_vezes_que_o_agente_passou_por_B))
        print('O agente passou pela posição C {} vezes.'.format(agente.contagem_de_vezes_que_o_agente_passou_por_C))
        print('O agente passou pela posição D {} vezes.'.format(agente.contagem_de_vezes_que_o_agente_passou_por_D))
        print('O agente passou pela posição E {} vezes.'.format(agente.contagem_de_vezes_que_o_agente_passou_por_E))
        print('---------------------------------------------')