#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io 
import pyboleto
from pyboleto.bank.bradesco import BoletoBradesco
from pyboleto.pdf import BoletoPDF
import datetime
pyboleto.unicode = str

def print_bradesco():
    listaDadosBradesco = []
    for i in range(2):
        d = BoletoBradesco()
        d.carteira = '06'  # Contrato firmado com o Banco Bradesco
        d.cedente = 'Empresa ACME LTDA'
        d.cedente_documento = "102.323.777-01"
        d.cedente_endereco = ("Rua Acme, 123 - Centro - Sao Paulo/SP - " +
                              "CEP: 12345-678")
        d.agencia_cedente = '0278-0'
        d.conta_cedente = '43905-3'
        d.especie_documento = "DM"
        d.data_vencimento = datetime.date(2022, 9, (25+i))
        d.data_documento = datetime.date(2022, 8, 17)
        d.data_processamento = datetime.date(2010, 2, 12)
        d.local_pagamento = "Pagável preferencialmente na Rede Bradesco ou Bradesco Expresso"
        d.instrucoes = [
            "- Linha 1",
            "- Sr Caixa, cobrar multa de 2% após o vencimento",
            "- Receber até 10 dias após o vencimento",
            ]
        d.demonstrativo = [
            "- Serviço Teste R$ 5,00",
            "- Total R$ 5,00",
            ]
        d.valor_documento = 2158.41+i
        d.valor_desconto = 1.90

        d.nosso_numero = "1112011668"
        d.numero_documento = "1112011668"
        d.cedente_logradouro = "AV NOSSA SENHORA APARECIDA, 456"
        d.cedente_bairro = "CENTRO CIVICO"
        d.cedente_cidade = "SANTO ANTONIO DA PLATINA"
        d.cedente_uf = "PR"
        d.cedente_cep = "87900-123"
        d.sacado = [
            "Cliente Teste %d" % (i + 1),
            "Rua Desconhecida, 00/0000 - Não Sei - Cidade - Cep. 00000-000",
            ""
            ]
        #d.logo_image = "ms-icon-150x150.png"
        d.conteudo_qr_code = '00020104141234567890123426580014BR.GOV.BCB.PIX0136123e4567-e12b-12d1-a456-42665544000027300012BR.COM.OUTRO011001234567895204000053039865406123.455802BR5917NOME DO RECEBEDOR6008BRASILIA61087007490062190515RP12345678-201980390012BR.COM.OUTRO01190123.ABCD.3456.WXYZ6304AD38'
        listaDadosBradesco.append(d)

#    # Bradesco Formato carne - duas paginas por folha A4
#    boleto = BoletoPDF('boleto-bradesco-formato-carne-teste.pdf', True)
#    for i in range(0, len(listaDadosBradesco), 2):
#        boleto.drawBoletoCarneDuplo(
#            listaDadosBradesco[i],
#            listaDadosBradesco[i + 1]
#        )
#        boleto.nextPage()
#    boleto.save()

    # Bradesco Formato normal - uma pagina por folha A4
    # boleto = BoletoPDF('boleto-bradesco.pdf')
    # for i in range(len(listaDadosBradesco)):
    #     boleto.drawBoleto(listaDadosBradesco[i])
    #     boleto.nextPage()
    # boleto.save()
    
    # usar um buffer para separar cada boleto(pagina) em um arquivo pdf individual
    # para envio ao cliente caso necessário    
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    with open(f'boleto_bradesco-{timestamp}.pdf', 'wb') as f: 
        buffer = io.BytesIO()
        boleto = BoletoPDF(buffer)
        for i in range(len(listaDadosBradesco)):                    
            boleto.drawBoleto(listaDadosBradesco[i])
            boleto.nextPage()
        boleto.save()
        f.write(buffer.getbuffer())

def print_all():
    print("Pyboleto version: %s" % pyboleto.__version__)
    print("----------------------------------")
    print("     Printing Example Boletos     ")
    print("----------------------------------")

    print("Bradesco")
    print_bradesco()

    print("----------------------------------")
    print("Ok")


if __name__ == "__main__":
    print_all()