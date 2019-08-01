from datetime import datetime
from motorcalculo import MotorCalculo

objMotor = MotorCalculo()

roteiro = []
roteiro.append('pcCorretagem = 32 / 100')
roteiro.append('pcRemuneracao = 2.35 / 100')
roteiro.append('pcProLabore = 0.65 / 100')
roteiro.append('pcIof = 0.38')
roteiro.append('pcTaxaNet = 0.63781')
roteiro.append('pcDesconto = 5 / 100')
roteiro.append('importancia_segurada = 10000')
roteiro.append('importancia_segurada = importancia_segurada * 3')
roteiro.append('premioNet = pcTaxaNet * importancia_segurada')
roteiro.append('premioTarifa = premioNet / 1-(pcCorretagem + pcRemuneracao + pcProLabore)')
roteiro.append('premioLiquido = premioTarifa - (premioTarifa * pcDesconto)')
roteiro.append('premioBruto = premioLiquido - (premioLiquido * pcIof)')
print(roteiro)

qtdCalculos = input("Quantidade de cálculos: ")
start_time = datetime.now()
i = 1
for i in range(qtdCalculos):
    result = objMotor.executar_roteiro(roteiro)
    # print(result)

end_time = datetime.now()
elapsed_time = end_time - start_time
elapsed_time = ((elapsed_time.seconds * 1000000) + elapsed_time.microseconds) // 1000

print('\nQuantidade de cálculos: {0} \nInício: {1} \nFim: {2} \nTempo total: {3} milissegundos'.format(qtdCalculos, start_time.strftime('%H:%M:%S.%f'), end_time.strftime('%H:%M:%S.%f'), elapsed_time))