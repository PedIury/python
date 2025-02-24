compra_confirmada = True
dados_compra = 'Compra no valor de 20 e entrega confirmada'


for enviar in range(3):
    if compra_confirmada:
     print(dados_compra)
     print('Detalhes enviados para seu email')
     break
else:
    print('falha na compra')    