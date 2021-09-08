import subprocess
import platform
from sys import stdout    # Para obter o nome do sistema operacional
from speedtest import Speedtest
from datetime import datetime

############################# DATA/HORA ###############################
datahora = (datetime.today().strftime('%d/%m/%Y %H:%M'))
out = open('resultado.txt', 'a')
out.write('\n------------------------------------------------------\n')
out.write('* DATA/HORA: ' + datahora)
out.write('\n------------------------------------------------------\n')
out.close()

############################### PING ##################################
out = open('resultado.txt', 'a')
out.write('* TESTE DE PING: \n')
out.close()


out = open('resultado.txt', 'a')
# Opção para o número de pacotes em função de
param = '-n' if platform.system().lower() == 'windows' else '-c'
subprocess.call(['ping', param, '3', '8.8.8.8'], stdout=out)
out.close()

############################ velocidade ###############################
out = open('resultado.txt', 'a')
out.write('\n------------------------------------------------------ \n')
out.write('* TESTE DE VELOCIDADE DE INTERNET:')
out.write('\n')
out.close()

out = open('resultado.txt', 'a')
speed_test = Speedtest()  # Chama o Speedtest
download = speed_test.download()  # Aciona o teste de velocidade de Download
upload = speed_test.upload()  # Aciona o teste de velocidade de Upload

download_speed = round(download / (10**6), 2)  # Converção para Mbps
result_download_speed = ("Velocidade de Download: " +
                         str(download_speed) + " Mbps")
print(result_download_speed)

upload_speed = round(upload / (10**6), 2)  # Converção para Mbps
result_upload_speed = ("Velocidade de Upload: " +
                       str(upload_speed) + " Mbps")
print(result_upload_speed)

out.write(str("\n" + result_download_speed))
out.write(str("\n" + result_upload_speed))
out.close()

############################ hardware ###############################
out = open('resultado.txt', 'a')
out.write('\n\n------------------------------------------------------ \n')
out.write("* INFORMACOES DO COMPUTADOR:")
out.write('\n')
out.close()


# TODO: Inserir resultado dos teste de velocidade no .txt
# TODO: Inserir as informações da máquina no .txt
