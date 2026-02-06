#BOT PARA MANDAR MENSAGEM DE NAMORO TODOS OS MESES
#BIBLIOTECAS:
import pywhatkit
''' biblioteca que automatiza o whatsapp '''
import datetime
''' biblioteca que analisa datas e horas'''

#CONFIGURAÇÕES
numero = '+554799626991'
dia_namoro = datetime.datetime.now()
hoje = datetime.datetime.now()

#MANDAR MENSAGEM:
if hoje.day == dia_namoro.day:
    pywhatkit.sendwhatmsg_instantly(
        phone_no = numero,
        message = 'olá, sou um bot programado pelo meu mestre Lorde Ruan.',
        wait_time = 10,
        tab_close = True
    )
    ''' 
        pywhatkit.sendwhatmsg_instantly: função que envia mensagem na hora
        phone_no: número que vai receber a mensagem
        message: mensagemkkkk
        wait_time: tempo que espera até enviar mensagem
        tab_close: fecha janela se estiver recebendo True
    '''