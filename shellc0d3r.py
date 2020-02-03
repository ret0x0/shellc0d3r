#!/usr/bin/python

# simple script to generate shellcodes given binaries, asm code, or c code (By @ret0x0)

# https://github.com/ret0x0/shellc0d3r

import commands
print('''

 ____  _          _ _       ___      _ _____      
/ ___|| |__   ___| | | ___ / _ \  __| |___ / _ __ 
\___ \| '_ \ / _ \ | |/ __| | | |/ _` | |_ \| '__|
 ___) | | | |  __/ | | (__| |_| | (_| |___) | |   
|____/|_| |_|\___|_|_|\___|\___/ \__,_|____/|_|   
                                                  

''')
print('''

-=[OPTIONS]=-
==========================
    1) From NASM to Shellcode
    2) From Binary to Shellcode
    3) From C to Shellcode
    4) Exit
    
''')

opt = raw_input('\033[1;34m[=]\033[0m Option: ')

if opt == '4':

    print('\033[1;34m[*]\033[0m Exiting')

elif opt == '1':

    pth = raw_input('\033[1;34m[=]\033[0m NASM File Path: ')
    
    commands.getoutput('nasm -felf64 ' + pth + ' -o shellcode.o')
    shellcode = commands.getoutput('''for i in $(objdump -d shellcode.o |grep "^ " |cut -f2); do echo -n '\\x'$i; done;echo''')
    
    print('\033[1;32m[+]\033[0m Shellcode generated successfully')
    print('    \033[1;34m[*]\033[0m Lenght = ' + str(len(shellcode.replace("\\x", ''))/2) + ' bytes')
    print('    \033[1;34m[*]\033[0m Shellcode = ' + shellcode)
    

elif opt == '2':

    pth = raw_input('\033[1;34m[=]\033[0m Binary File Path: ')
    shellcode = commands.getoutput('''for i in $(objdump -d ''' + pth + ''' |grep "^ " |cut -f2); do echo -n '\\x'$i; done;echo''')
    
    print('\033[1;32m[+]\033[0m Shellcode generated successfully')
    print('    \033[1;34m[*]\033[0m Lenght = ' + str(len(shellcode.replace("\\x", ''))/2) + ' bytes')
    print('    \033[1;34m[*]\033[0m Shellcode = ' + shellcode)

elif opt == '3':

    pth = raw_input('\033[1;34m[=]\033[0m C File Path: ')
    
    commands.getoutput('gcc -pthread ' + pth + ' -o shellcode')
    shellcode = commands.getoutput('''for i in $(objdump -d shellcode |grep "^ " |cut -f2); do echo -n '\\x'$i; done;echo''')
    
    print('\033[1;32m[+]\033[0m Shellcode generated successfully')
    print('    \033[1;34m[*]\033[0m Lenght = ' + str(len(shellcode.replace("\\x", ''))/2) + ' bytes')
    print('    \033[1;34m[*]\033[0m Shellcode = ' + shellcode)

else:

    print('\033[1;31m[-]\033[0m Unknown option')
