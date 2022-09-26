# -*- coding: utf-8 -*-
from ..data import BoletoException
BANCOS_IMPLEMENTADOS = {
    '001': 'bancodobrasil.BoletoBB',
    '003': 'bancodaamazonia.BoletoBancodaAmazonia',
    '004': 'banconordeste.BoletoBancoNordeste',
    '033': 'santander.BoletoSantander',
    '041': 'banrisul.BoletoBanrisul',
    '047': 'banese.BoletoBanese',
    '070': 'brb.BoletoBrb',
    '077': 'bancointer.BoletoInter',
    '383': 'juno.BoletoJuno',
    '104': 'caixa.BoletoCaixa',
    '136': 'unicred.BoletoUnicred',
    '099': 'pagfacil.BoletoPagFacil',
    '104sigcb': 'caixa.BoletoCaixaSIGCB',
    '104sigcb2': 'caixa.BoletoCaixaSIGCB2',
    '104v2': 'caixa.BoletoCaixaV2',
    '237': 'bradesco.BoletoBradesco',
    '341': 'itau.BoletoItau',
    '356': 'real.BoletoReal',
    '399': 'hsbc.BoletoHsbc',
    '422': 'safra.BoletoSafra',
    '748': 'sicredi.BoletoSicredi',
    '748unicredi': 'sicredi.BoletoUnicredi',
    '756': 'sicoob.BoletoSicoob',
    # '085': 'cecred.BoletoCecred',
    '085': 'ailos.BoletoAilos',
    '218': 'bonsucesso.BoletoBonSucesso',
    '133': 'cresol.BoletoCresol',
    'localgateway': 'localgateway.BoletoLocalGateway',
    'arrecadacao': 'febraban.BoletoArrecadacao',
}


def get_class_for_codigo(banco_codigo):
    """Retorna a classe que implementa o banco

    :param banco_codigo:
    :type banco_codigo: string
    :return: Classo do Banco subclasse de :class:`pyboleto.data.BoletoData`
    :rtype: :class:`pyboleto.data.BoletoData`
    """
    try:
        banco = BANCOS_IMPLEMENTADOS[banco_codigo].split('.')
    except KeyError:
        raise(BoletoException('Este banco não é suportado.'))

    mod = __import__('pyboleto.bank.' + banco[0],
                     globals(), locals(), [banco[1]])

    return getattr(mod, banco[1])
