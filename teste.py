import subprocess
import platform    # Para obter o nome do sistema operacional
from speedtest import Speedtest

############################### PING ##################################
out = open('resultado.txt', 'a')

# Opção para o número de pacotes em função de
param = '-n' if platform.system().lower() == 'windows' else '-c'
subprocess.call(['ping', param, '10', '8.8.8.8'], stdout=out)

############################ velocidade ###############################
speed_test = Speedtest()  # Chama o Speedtest
download = speed_test.download()  # Aciona o teste de velocidade de Download
upload = speed_test.upload()  # Aciona o teste de velocidade de Upload

download_speed = round(download / (10**6), 2)  # Converção para Mbps
result_download_speed = ("Velocidade de Download: " +
                         str(download_speed) + " Mbps",)

upload_speed = round(upload / (10**6), 2)  # Converção para Mbps
result_upload_speed = ("Velocidade de Upload: " +
                       str(upload_speed) + " Mbps")
out.close()

# TODO: Inserir resultado dos teste de velocidade no .txt
# TODO: Inserir as informações da máquina no .txt
