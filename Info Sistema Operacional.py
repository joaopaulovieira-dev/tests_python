
import os
import sys
orig_stdout = sys.stdout
out = open('resultado.txt', 'a', encoding='utf8')
sys.stdout = out

for line in os.popen('systeminfo'):
    print(line.rstrip())

sys.stdout = orig_stdout
out.close()
