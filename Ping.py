import platform    # Para obter o nome do sistema operacional
import subprocess  # Para executar um comando shell

# Opção para o número de pacotes em função de
param = '-n' if platform.system().lower() == 'windows' else '-c'

# Construindo o comando. Ex: "ping -c 1 google.com"
command = ['ping', param, '5', '8.8.8.8']

print(subprocess.call(command) == 0)
