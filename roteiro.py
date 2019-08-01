
pcCorretagem = 32 / 100
pcRemuneracao = 2.35 / 100
pcProLabore = 0.65 / 100
pcIof = 0.38
pcTaxa = 0.63781
pcDesconto = 5 / 100
importancia_segurada = 10000
importancia_segurada = importancia_segurada * 3
premioNet = pcTaxa * importancia_segurada
premioTarifa = premioNet / 1-(pcCorretagem + pcRemuneracao + pcProLabore)
premioLiquido = premioTarifa - (premioTarifa * pcDesconto)
premioBruto = premioLiquido - (premioLiquido * pcIof)
# print('Prêmio Bruto: {}'.format(premioBruto))