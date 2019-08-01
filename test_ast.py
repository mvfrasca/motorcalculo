import ast
from datetime import datetime

with open("roteiro.py", "r") as source:
    tree = ast.parse(source.read())

co = compile(tree, "<ast>", 'exec')

qtdCalculos = int(input("Quantidade de cálculos: "))
start_time = datetime.now()
i = 1
for i in range(qtdCalculos):
    exec(co)

end_time = datetime.now()
elapsed_time = end_time - start_time
elapsed_time = ((elapsed_time.seconds * 1000000) + elapsed_time.microseconds) // 1000

print('\nQuantidade de cálculos: {0} \nInício: {1} \nFim: {2} \nTempo total: {3} milissegundos'.format(qtdCalculos, start_time.strftime('%H:%M:%S.%f'), end_time.strftime('%H:%M:%S.%f'), elapsed_time))
