from iniciando import inicio, login
from falas_fixas import login_negado, login_permitido
import sys
import utils
import pedidos


inicio()
if not login():
    login_negado()
    sys.exit()
else:
    login_permitido()

i = [1, 2]  # Temporario para printar o pedido apenas 2 vezes

while True:
    pedido = utils.ouvir_microfone()
    
    # Laço for temporário para printar o pedido apenas 2 vezes
    for n in i:
        print(utils.formatar_pedido(pedido))
        i.append('a')
        if len(i) > 3:
            break
    
    if utils.formatar_pedido(pedido) == "encerrar":
        pedido = "encerrar"
        utils.encerrar_kronos()
        utils.animacao_encerrar_kronos()
        sys.exit()
    elif utils.formatar_pedido(pedido) == "abriryoutube":
        pedidos.abrir_youtube()
    elif utils.formatar_pedido(pedido) == "abrirfacebook":
        pedidos.abrir_facebook()
    elif utils.formatar_pedido(pedido) == "abrirvagas":
        pedidos.abrir_vagas()
    elif utils.formatar_pedido(pedido) == "abrirchrome":
        pedidos.abrir_chrome()

print("Fora do laço while True")
