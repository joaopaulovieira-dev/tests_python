import platform    # Para obter o nome do sistema operacional
import subprocess  # Para executar um comando shell
import sys

# Opção para o número de pacotes em função de
param = '-n' if platform.system().lower() == 'windows' else '-c'

# Construindo o comando. Ex: "ping -c 1 google.com"
command = ['ping', param, '5', '8.8.8.8']

print(subprocess.call(command) == 0)

# Função que guarda o resultado em uma variavel


def ping():

    cmd = subprocess.Popen(
        ["ping", "8.8.8.8"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    stdout, stderr = cmd.communicate()
    ping_label = stdout
    if stderr == None:
        print(stdout)

    else:
        print(stderr)
        sys.exit(1)
