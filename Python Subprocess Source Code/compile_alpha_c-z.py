import os
import shutil
import fileinput
import time
import subprocess

info = subprocess.STARTUPINFO()
info.dwFlags = 1
info.wShowWindow = 0

alpha_led = [53,
             40,
             28,
             41,
             42,
             43,
             33,
             44,
             45,
             46,
             57,
             56,
             34,
             35,
             26,
             29,
             39,
             30,
             32,
             54,
             27,
             52,
             31,
             51]

alpha_str = ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']

target_str = ["print('[NAME]: kb_alpha_",
              "{53:"]

led_alpha_file = 'kb_alpha.pyw'
if os.path.exists(led_alpha_file):
    print('-- found:', led_alpha_file)

i = 0
for _ in alpha_str:
    new_name = os.path.join(os.getcwd() + '\\kb_alpha_' + alpha_str[i] + '.pyw')
    print('-- creating:', new_name)
    shutil.copy(led_alpha_file, new_name)

    for line in fileinput.input(new_name, inplace=True):
        print(line.rstrip().replace(target_str[0], str(target_str[0] + alpha_str[i]))),

    for line in fileinput.input(new_name, inplace=True):
        print(line.rstrip().replace(target_str[1], str('{' + str(alpha_led[i]) + ':'))),

    time.sleep(0.5)

    cmd = ('pyinstaller -F ' + '.\\kb_alpha_' + alpha_str[i] + '.pyw')
    xcmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    i += 1

print('-- complete. any subprocesses if any will take a moment to complete.')
input('\nPress any key to quit.')

