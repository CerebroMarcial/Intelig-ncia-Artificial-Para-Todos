from Enum_posicoes_existentes_no_ambiente_de_tarefa import Enum_posicoes_existentes_no_ambiente_de_tarefa

class Agente():
    percepcao_atual=[]
    posicao_do_agente_naquele_momento=Enum_posicoes_existentes_no_ambiente_de_tarefa.A.value
    guia_inicial_dada_pelo_programador_com_as_instrucoes_que_o_aspirador_de_po_tem_que_consultar_pra_saber_o_que_fazer={
        "['A, Limpo']":'Direita',
        "['A, Sujo']":'Aspirar',
        "['B, Limpo']":'Esquerda',
        "['B, Sujo']":'Aspirar'
        }
    def agente_reativo_simples(self,percepcao):
        self.percepcao_atual.append(self.posicao_do_agente_naquele_momento+', '+percepcao)
        print('O agente está consultando a tabela com as instrucoes para saber o que fazer.')
        decisao_a_ser_executada=self.refletir_o_que_deve_ser_feito_acessando_o_guia_com_as_instrucoes(self.percepcao_atual,self.guia_inicial_dada_pelo_programador_com_as_instrucoes_que_o_aspirador_de_po_tem_que_consultar_pra_saber_o_que_fazer)
        print('A decisao tomada foi: {}'.format(decisao_a_ser_executada))
        return decisao_a_ser_executada

    def se_locomovendo_para_a_esquerda(self,local_pretendido):
        print('**ligando o motor das rodas do aspirador**')
        print('** FZENDO BARULHO ** VRUUUMMMM ')
        print('O aspirador se locomoveu para a posicao {}'.format(local_pretendido))

    def se_locomovendo_para_a_direita(local_pretendido):
        print('**ligando o motor das rodas do aspirador**')
        print('** FZENDO BARULHO ** VRUUUMMMM ')
        print('O aspirador se locomoveu para a posicao {}'.format(local_pretendido))
        self.posicao_do_agente_naquele_momento=local_pretendido
        
    def aspirando_sujeira(self,posicao_do_agente):
        print('**ligando o motor do aspirador**')
        print('** FZENDO BARULHO ** BZZZZZZZZZZZZZZZZZZZZZ ')
        print('O aspirador está retirando sujeira na posicao {}'.format(self.posicao_do_agente_naquele_momento))

    def refletir_o_que_deve_ser_feito_acessando_o_guia_com_as_instrucoes(self,percepcao_atual,guia_inicial_dada_pelo_programador_com_as_instrucoes_que_o_aspirador_de_po_tem_que_consultar_pra_saber_o_que_fazer):
        print('A percepcao atual é {}'.format(str(self.percepcao_atual[-1])))
        return self.guia_inicial_dada_pelo_programador_com_as_instrucoes_que_o_aspirador_de_po_tem_que_consultar_pra_saber_o_que_fazer[str("['{}']".format(self.percepcao_atual[-1]))]