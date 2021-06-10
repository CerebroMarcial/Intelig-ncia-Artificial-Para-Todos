
class Respaldo_ao_programador():
    def imprimir_o_que_esta_acontecendo(self,agente,ambiente,contagem_de_percepcoes):
        print('Início do novo ciclo!\nEssa é a {}° percepcao do agente'.format(contagem_de_percepcoes))
        print('O agente está na posicao {}'.format(agente.posicao_do_agente_naquele_momento))
        print('A configuracao do tabuleiro está assim : {}'.format(ambiente.configuraçao_do_ambiente))
        print('---------------------------------------------')